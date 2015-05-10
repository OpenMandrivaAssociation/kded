%define major 5
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kded
Version: 5.10.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Source100: %{name}.rpmlintrc
Summary: Extensible deamon for providing system level services
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5Init)
BuildRequires: cmake(KF5Service)

%description
Extensible deamon for providing system level services.

%package devel
Summary: Development files for the KDE Frameworks 5 service daemon
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}

%description devel
Development files for the KDE Frameworks 5 service daemon.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_bindir}/kded5
%{_datadir}/kservicetypes5/*
%{_datadir}/dbus-1/*/*
%{_libdir}/libkdeinit5_kded5.so
%{_mandir}/man8/*
%lang(ca) %{_mandir}/ca/man8/*
%lang(it) %{_mandir}/it/man8/*
%lang(nl) %{_mandir}/nl/man8/*
%lang(pt_BR) %{_mandir}/pt_BR/man8/*
%lang(ru) %{_mandir}/ru/man8/*
%lang(sv) %{_mandir}/sv/man8/*
%lang(uk) %{_mandir}/uk/man8/*

%files devel
%{_libdir}/cmake/KDED
