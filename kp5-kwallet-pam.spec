#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.25.0
%define		qtver		5.9.0
%define		kpname		kwallet-pam
Summary:	KWallet PAM integration
Name:		kp5-%{kpname}
Version:	5.25.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		Base
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	6f58568d80e2d97e14b1fa0cef8ea938
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
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DCMAKE_INSTALL_LIBDIR:PATH=/%{_lib} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	..
%ninja_build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /%{_lib}/security/pam_kwallet5.so
/etc/xdg/autostart/pam_kwallet_init.desktop
%attr(755,root,root) %{_libexecdir}/pam_kwallet_init
%{systemduserunitdir}/plasma-kwallet-pam.service
