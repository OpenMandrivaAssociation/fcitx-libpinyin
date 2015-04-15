%define beta %{nil}
%define scmrev %{nil}

Name: fcitx-libpinyin
Version: 0.3.1
%if "%{beta}" == ""
%if "%{scmrev}" == ""
Release: 1
Source0: http://downloads.fcitx-im.org/%{name}/%{name}-%{version}_dict.tar.xz
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
BuildRequires: pkgconfig(fcitx)
BuildRequires: pkgconfig(libpinyin) libpinyin
BuildRequires: pkgconfig(QtWebKit)

%track
prog %{name} = {
	url = http://downloads.fcitx-im.org/%{name}
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
