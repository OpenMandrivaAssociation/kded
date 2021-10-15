%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

# (tpg) optimize it a bit
%global optflags %{optflags} -O3

Name: kded
Version:	5.87.0
Release:	1
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
%find_lang %{name} --all-name --with-man

%files -f %{name}.lang
%{_datadir}/qlogging-categories5/*.*categories
%{_bindir}/kded5
%{_datadir}/kservicetypes5/*
%{_datadir}/applications/org.kde.kded5.desktop
%{_datadir}/dbus-1/*/*
%{_mandir}/man8/*
%{_prefix}/lib/systemd/user/plasma-kded.service

%files devel
%{_libdir}/cmake/KDED
