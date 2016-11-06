%define 	modulename pam_abl
Summary:	PAM abl module
Summary(pl.UTF-8):	Moduł PAM automatycznie dopisujący do blacklisty
Name:		pam-%{modulename}
Version:	0.6.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/pam-abl/pam-abl-%{version}.tar.gz
# Source0-md5:	62e02b88cf2da09eeea101a99f69f1ee
URL:		http://pam-abl.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	db-devel >= 4.4.20
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
%setup -q -c -n pam-abl-%{version}

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/security,/%{_lib}/security,%{_sbindir},/var/lib/abl}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -p conf/pam_abl.conf $RPM_BUILD_ROOT/etc/security

%{__mv} $RPM_BUILD_ROOT{%{_bindir},%{_sbindir}}/pam_abl
%{__mv} $RPM_BUILD_ROOT{%{_prefix}/lib,/%{_lib}}/security/pam_abl.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog.txt README doc/pam_abl.*.txt
%attr(755,root,root) /%{_lib}/security/pam_abl.so
%attr(755,root,root) %{_sbindir}/pam_abl
%config(noreplace) %verify(not md5 mtime size) /etc/security/pam_abl.conf
%attr(700,root,root) %dir /var/lib/abl
#%%{_mandir}/man1/pam_abl.1*
#%%{_mandir}/man5/pam_abl.conf.5*
#%%{_mandir}/man8/pam_abl.8*
