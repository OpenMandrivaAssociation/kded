%define major 5
%define debug_package %{nil}

Name: kded
Version: 4.99.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
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
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_bindir}/kded5
%{_datadir}/kservicetypes5/*
%{_datadir}/dbus-1/*/*
%{_libdir}/libkdeinit5_kded5.so
%{_mandir}/man8/*

%files devel
%{_libdir}/cmake/KDED
