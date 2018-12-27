%define		kdeplasmaver	5.14.4
%define		qtver		5.3.2
%define		kpname		kwallet-pam
Summary:	KWallet PAM integration
Name:		kp5-%{kpname}
Version:	5.14.4
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		Base
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	d548ae1d4b1850cc65093128a411304a
URL:		http://www.kde.org/
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	pam-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KWallet PAM integration.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DCMAKE_INSTALL_LIBDIR:PATH=/%{_lib} \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/pam_kwallet5.so
/etc/xdg/autostart/pam_kwallet_init.desktop
%attr(755,root,root) %{_libexecdir}/pam_kwallet_init
