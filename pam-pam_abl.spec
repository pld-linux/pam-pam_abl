# TODO: optflags
%define 	modulename pam_abl
Summary:	PAM abl module
Summary(pl):	Modu³ PAM automatycznie dopisuj±cy do blacklisty
Name:		pam-%{modulename}
Version:	0.2.3
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/pam-abl/pam_abl-%{version}.tar.gz
# Source0-md5:	fbcf97067e9647fa1d9257d4e6133cba
URL:		http://www.hexten.net/pam_abl/
BuildRequires:	pam-devel
Obsoletes:	pam_abl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM module which provides auto blacklisting of hosts and users
responsible for repeated failed authentication attempts.

%description -l pl
Modu³ PAM automatycznie dopisuj±cy do blacklisty hosty i u¿ytkowników
po wykryciu powtarzaj±cych siê b³êdów uwierzytelnienia.

%prep
%setup -q -n %{modulename}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/security,/%{_lib}/security,%{_sbindir},/var/lib/abl}

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
