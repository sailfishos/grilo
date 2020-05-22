Name:       libgrilo
Summary:    Framework for discovering and browsing media
Version:    0.3.12
Release:    1
License:    LGPLv2
URL:        https://live.gnome.org/Grilo
Source0:    http://ftp.gnome.org/pub/GNOME/sources/grilo/0.3/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(totem-plparser)
BuildRequires:  pkgconfig(python)
BuildRequires:  intltool
BuildRequires:  gnome-common
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  vala-devel

%description
Grilo is a framework focused on making media discovery and browsing
easy for application developers.
More precisely, Grilo provides:
* A single, high-level API that abstracts the differences among
  various media content providers, allowing application developers
  to integrate content from various services and sources easily.
* A collection of plugins for accessing content from various media
  providers. Developers can share efforts and code by writing
  plugins for the framework that are application agnostic.
* A flexible API that allows plugin developers to write plugins of
  various kinds.


%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
%description devel
Development files for %{name}

%package -n grilo-tools
Summary:    Tools for grilo
Requires:   %{name} = %{version}-%{release}
%description -n grilo-tools
Tools for grilo

%prep
%autosetup -p1 -n %{name}-%{version}/grilo

%build
%meson -Denable-introspection=false -Denable-gtk-doc=false -Denable-test-ui=false

%install
rm -rf %{buildroot}
%meson_install
%find_lang grilo --with-gnome

%files -f grilo.lang
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/*.so.*
%{_datadir}/vala/vapi/grilo*.deps
%{_datadir}/vala/vapi/grilo*.vapi

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_libdir}/girepository-1.0/*.typelib
%{_datadir}/gir-1.0/*.gir

%files -n grilo-tools
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/*/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
