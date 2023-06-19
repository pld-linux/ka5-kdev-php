#
# Conditional build:
%bcond_with	tests		# build with tests

%define		kdeappsver	23.04.2
%define		kframever	5.103.0
%define		qtver		5.15.2
%define		kaname		kdev-php

Summary:	KDE Integrated Development Environment - php
Summary(pl.UTF-8):	Zintegrowane środowisko programisty dla KDE - php
Name:		ka5-%{kaname}
Version:	23.04.2
Release:	2
License:	GPL
Group:		X11/Development/Tools
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	42f73dd2afb5874134750e942a033938
URL:		http://www.kdevelop.org/
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel >= 5.15.2
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.15.2
BuildRequires:	gettext-devel
BuildRequires:	ka5-kdevelop-devel >= 5.7
BuildRequires:	ka5-kdevelop-pg-qt
BuildRequires:	kf5-extra-cmake-modules >= 5.78.0
BuildRequires:	kf5-kauth-devel >= 5.105.0
BuildRequires:	kf5-kcodecs-devel >= 5.105.0
BuildRequires:	kf5-kcompletion-devel >= 5.105.0
BuildRequires:	kf5-kconfigwidgets-devel >= 5.105.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.105.0
BuildRequires:	kf5-ki18n-devel >= 5.105.0
BuildRequires:	kf5-kitemviews-devel >= 5.105.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.105.0
BuildRequires:	kf5-kparts-devel >= 5.105.0
BuildRequires:	kf5-kservice-devel >= 5.105.0
BuildRequires:	kf5-ktexteditor-devel >= 5.91.0
BuildRequires:	kf5-ktextwidgets-devel >= 5.105.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.105.0
BuildRequires:	kf5-kxmlgui-devel >= 5.105.0
BuildRequires:	kf5-solid-devel >= 5.105.0
BuildRequires:	kf5-sonnet-devel >= 5.105.0
BuildRequires:	kf5-syntax-highlighting-devel >= 5.105.0
BuildRequires:	kf5-threadweaver-devel >= 5.91.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	ka5-kdevelop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE Integrated Development Environment - php.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DFORCE_BASH_COMPLETION_INSTALLATION=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%{_includedir}/kdev-php
%{_libdir}/cmake/KDevPHP
%attr(755,root,root) %{_libdir}/libkdevphpcompletion.so
%attr(755,root,root) %{_libdir}/libkdevphpduchain.so
%attr(755,root,root) %{_libdir}/libkdevphpparser.so
%dir %{_libdir}/qt5/plugins/kdevplatform/511/kcm
%attr(755,root,root) %{_libdir}/qt5/plugins/kdevplatform/511/kcm/kcm_kdevphpdocs.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kdevplatform/511/kdevphpdocs.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kdevplatform/511/kdevphplanguagesupport.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kdevplatform/511/kdevphpunitprovider.so
%{_datadir}/kdevappwizard/templates/simple_phpapp.tar.bz2
%dir %{_datadir}/kdevphpsupport
%{_datadir}/kdevphpsupport/phpfunctions.php
%{_datadir}/kdevphpsupport/phpunitdeclarations.php
%{_datadir}/kservices5/kcm_kdevphpdocs.desktop
%{_datadir}/metainfo/org.kde.kdev-php.metainfo.xml
%{_datadir}/qlogging-categories5/kdevphpsupport.categories
