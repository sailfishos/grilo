Name:       grilo
Summary:    Content discovery framework
Version:    0.3.15
Release:    1
License:    LGPLv2+
URL:        https://wiki.gnome.org/Projects/Grilo
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  meson >= 0.46.0
BuildRequires:  vala-devel >= 0.27.1
BuildRequires:  gettext
BuildRequires:  python3-base
BuildRequires:  pkgconfig(gio-2.0) >= 2.58
BuildRequires:  pkgconfig(glib-2.0) >= 2.58
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.58
BuildRequires:  pkgconfig(gobject-2.0) >= 2.58
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.41.3
BuildRequires:  pkgconfig(totem-plparser) >= 3.4.1
Obsoletes:      libgrilo

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
Summary:    Libraries/include files for Grilo framework
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%package tools
Summary:    Tools for Grilo framework
Requires:   %{name} = %{version}-%{release}

%description tools
Tools for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/grilo

%build
%meson -Denable-gtk-doc=false -Denable-test-ui=false -Dsoup3=false
%meson_build

%install
%meson_install
%find_lang grilo --with-gnome

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f grilo.lang
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS NEWS README.md TODO
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_libdir}/girepository-1.0/*.typelib
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/grilo*.deps
%{_datadir}/vala/vapi/grilo*.vapi

%files tools
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
