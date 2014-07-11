%define beta %{nil}
%define scmrev %{nil}

Name: fcitx-libpinyin
Version: 0.2.92
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 7
Source0: http://fcitx.googlecode.com/files/%{name}-%{version}_dict.tar.xz
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
URL: http://fcitx.googlecode.com/
License: GPLv2
Group: System/Internationalization
BuildRequires: cmake
BuildRequires: pkgconfig(fcitx)
BuildRequires: pkgconfig(libpinyin) libpinyin

%track
prog %{name} = {
	url = http://code.google.com/p/fcitx/downloads/list
	regex = %name-(__VER__)_dict\.tar\.xz
	version = %{version}
}

%description
LibPinYin IM plugin for fcitx

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
%_datadir/fcitx/addon/*
%_datadir/fcitx/configdesc/*
%_datadir/fcitx/inputmethod/*
%_datadir/fcitx/libpinyin
%_datadir/icons/*/*/*/*
