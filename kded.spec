%define major 5
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kded
Version: 5.4.0
Release: 2
Source0: http://ftp5.gwdg.de/pub/linux/kde/%{stable}/frameworks/%{version}/%{name}-%{version}.tar.xz
Source100: %{name}.rpmlintrc
Summary: Extensible deamon for providing system level services
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Init)
BuildRequires: cmake(KF5Service)
BuildRequires: ninja

%description
Extensible deamon for providing system level services

%package devel
Summary: Development files for the KDE Frameworks 5 service daemon
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}

%description devel
Development files for the KDE Frameworks 5 service daemon

%prep
%setup -q
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install

%files
%{_bindir}/kded5
%{_datadir}/kservicetypes5/*
%{_datadir}/dbus-1/*/*
%{_libdir}/libkdeinit5_kded5.so
%{_mandir}/man8/*
%lang(it) %{_mandir}/it/man8/*
%lang(nl) %{_mandir}/nl/man8/*
%lang(pt_BR) %{_mandir}/pt_BR/man8/*
%lang(ru) %{_mandir}/ru/man8/*
%lang(sv) %{_mandir}/sv/man8/*
%lang(uk) %{_mandir}/uk/man8/*

%files devel
%{_libdir}/cmake/KDED
