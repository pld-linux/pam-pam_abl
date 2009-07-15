#
# TODO:
#	- pass proper dirs to configure
#	- cleanup install
#
%define 	modulename pam_abl
Summary:	PAM abl module
Summary(pl.UTF-8):	Moduł PAM automatycznie dopisujący do blacklisty
Name:		pam-%{modulename}
Version:	0.3.0
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	http://pam-abl.deksai.com/downloads/pam-abl-%{version}.tar.bz2
# Source0-md5:	76b00cc5a2d91a7419b673da51c8e775
URL:		http://pam-abl.deksai.com/
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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/security,/%{_lib}/security,%{_sbindir},/var/lib/abl}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install pam_abl.so $RPM_BUILD_ROOT/%{_lib}/security
install conf/pam_abl.conf $RPM_BUILD_ROOT/etc/security/pam_abl.conf
install tools/pam_abl $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/copying.html doc/index.html doc/pam_abl.html doc/style.css
%attr(755,root,root) /%{_lib}/security/pam_abl.so
%attr(755,root,root) %{_sbindir}/pam_abl
%config(noreplace) %verify(not md5 mtime size) /etc/security/pam_abl.conf
%attr(700,root,root) %dir /var/lib/abl
