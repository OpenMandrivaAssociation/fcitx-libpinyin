%define beta %{nil}
%define scmrev %{nil}

Name: fcitx-libpinyin
Version: 0.5.3
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 2
Source0: http://download.fcitx-im.org/%{name}/%{name}-%{version}_dict.tar.xz
%else
Release: 0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%else
%if "%{scmrev}" == ""
Release: 0.%{beta}.1
Source0: %{name}-%{version}%{beta}.tar.bz2
%else
Release: 0.%{beta}.0.%{scmrev}.1
Source0: %{name}-%{scmrev}.tar.xz
%endif
%endif
Summary: LibPinYin IM plugin for fcitx
URL: http://www.fcitx-im.org
License: GPLv2
Group: System/Internationalization
BuildRequires: cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5WebEngineWidgets) cmake(Qt5Network) cmake(Qt5DBus)
BuildRequires: cmake(FcitxQt5DBusAddons)
BuildRequires: cmake(FcitxQt5WidgetsAddons)
BuildRequires: pkgconfig(fcitx)
BuildRequires: pkgconfig(libpinyin) libpinyin
BuildRequires: pkgconfig(dbus-1)

%description
LibPinYin IM plugin for fcitx.

%prep
%if "%{scmrev}" == ""
%setup -q -n %{name}-%{version}%{beta}
%else
%setup -q -n %{name}
%endif

%build
%cmake
%make

%install
%makeinstall_std -C build
%find_lang %name

%files -f %name.lang
%_libdir/fcitx/*.so
%_libdir/fcitx/qt/*.so
%_datadir/fcitx/addon/*
%_datadir/fcitx/configdesc/*
%_datadir/fcitx/inputmethod/*
%_datadir/fcitx/libpinyin
%_datadir/fcitx/imicon/*
%_datadir/icons/*/*/*/*
