%define 	modulename pam_abl
Summary:	PAM abl module
Summary(pl.UTF-8):	Moduł PAM automatycznie dopisujący do blacklisty
Name:		pam-%{modulename}
Version:	0.4.3
Release:	3
License:	GPL v2
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/pam-abl/pam-abl-%{version}.tar.bz2
# Source0-md5:	62008b6eb8aa2c93bdb53c4f848bfb93
Patch0:		%{name}-conf.patch
URL:		http://pam-abl.deksai.com/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	pam-devel
Obsoletes:	pam_abl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM module which provides auto blacklisting of hosts and users
responsible for repeated failed authentication attempts.

%description -l pl.UTF-8
Moduł PAM automatycznie dopisujący do blacklisty hosty i użytkowników
po wykryciu powtarzających się błędów uwierzytelnienia.

%prep
%setup -q -n pam-abl-%{version}
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-pam-dir=/%{_lib}/security
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/security,%{_sbindir},/var/lib/abl}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install conf/pam_abl.conf $RPM_BUILD_ROOT/etc/security

%{__mv} $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}/pam_abl

# packaged in %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/pam-abl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS conf/system-auth
%attr(755,root,root) /%{_lib}/security/pam_abl.so
%attr(755,root,root) %{_sbindir}/pam_abl
%config(noreplace) %verify(not md5 mtime size) /etc/security/pam_abl.conf
%attr(700,root,root) %dir /var/lib/abl
%{_mandir}/man1/pam_abl.1*
%{_mandir}/man5/pam_abl.conf.5*
%{_mandir}/man8/pam_abl.8*
