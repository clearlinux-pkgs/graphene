#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : graphene
Version  : 1.8.2
Release  : 7
URL      : https://download.gnome.org/sources/graphene/1.8/graphene-1.8.2.tar.xz
Source0  : https://download.gnome.org/sources/graphene/1.8/graphene-1.8.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: graphene-data
Requires: graphene-lib
Requires: graphene-bin
Requires: graphene-license
BuildRequires : glib-dev
BuildRequires : glibc-bin
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : meson
BuildRequires : ninja
BuildRequires : python3

%description
# Graphene
###  A thin layer of types for graphic libraries
[![Build Status](https://travis-ci.org/ebassi/graphene.svg?branch=master)](https://travis-ci.org/ebassi/graphene)
[![Build status](https://ci.appveyor.com/api/projects/status/pw7o5grgko1l06hd/branch/master?svg=true)](https://ci.appveyor.com/project/ebassi/graphene/branch/master)

%package bin
Summary: bin components for the graphene package.
Group: Binaries
Requires: graphene-data
Requires: graphene-license

%description bin
bin components for the graphene package.


%package data
Summary: data components for the graphene package.
Group: Data

%description data
data components for the graphene package.


%package dev
Summary: dev components for the graphene package.
Group: Development
Requires: graphene-lib
Requires: graphene-bin
Requires: graphene-data
Provides: graphene-devel

%description dev
dev components for the graphene package.


%package lib
Summary: lib components for the graphene package.
Group: Libraries
Requires: graphene-data
Requires: graphene-license

%description lib
lib components for the graphene package.


%package license
Summary: license components for the graphene package.
Group: Default

%description license
license components for the graphene package.


%prep
%setup -q -n graphene-1.8.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528992634
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/doc/graphene
cp LICENSE %{buildroot}/usr/share/doc/graphene/LICENSE
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/installed-tests/graphene-1.0/box
/usr/libexec/installed-tests/graphene-1.0/euler
/usr/libexec/installed-tests/graphene-1.0/frustum
/usr/libexec/installed-tests/graphene-1.0/matrix
/usr/libexec/installed-tests/graphene-1.0/plane
/usr/libexec/installed-tests/graphene-1.0/point
/usr/libexec/installed-tests/graphene-1.0/point3d
/usr/libexec/installed-tests/graphene-1.0/quad
/usr/libexec/installed-tests/graphene-1.0/quaternion
/usr/libexec/installed-tests/graphene-1.0/ray
/usr/libexec/installed-tests/graphene-1.0/rect
/usr/libexec/installed-tests/graphene-1.0/simd
/usr/libexec/installed-tests/graphene-1.0/size
/usr/libexec/installed-tests/graphene-1.0/sphere
/usr/libexec/installed-tests/graphene-1.0/triangle
/usr/libexec/installed-tests/graphene-1.0/vec2
/usr/libexec/installed-tests/graphene-1.0/vec3
/usr/libexec/installed-tests/graphene-1.0/vec4

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Graphene-1.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/installed-tests/graphene-1.0/box.test
/usr/share/installed-tests/graphene-1.0/euler.test
/usr/share/installed-tests/graphene-1.0/frustum.test
/usr/share/installed-tests/graphene-1.0/matrix.test
/usr/share/installed-tests/graphene-1.0/plane.test
/usr/share/installed-tests/graphene-1.0/point.test
/usr/share/installed-tests/graphene-1.0/point3d.test
/usr/share/installed-tests/graphene-1.0/quad.test
/usr/share/installed-tests/graphene-1.0/quaternion.test
/usr/share/installed-tests/graphene-1.0/ray.test
/usr/share/installed-tests/graphene-1.0/rect.test
/usr/share/installed-tests/graphene-1.0/simd.test
/usr/share/installed-tests/graphene-1.0/size.test
/usr/share/installed-tests/graphene-1.0/sphere.test
/usr/share/installed-tests/graphene-1.0/triangle.test
/usr/share/installed-tests/graphene-1.0/vec2.test
/usr/share/installed-tests/graphene-1.0/vec3.test
/usr/share/installed-tests/graphene-1.0/vec4.test

%files dev
%defattr(-,root,root,-)
/usr/include/graphene-1.0/graphene-box.h
/usr/include/graphene-1.0/graphene-euler.h
/usr/include/graphene-1.0/graphene-frustum.h
/usr/include/graphene-1.0/graphene-gobject.h
/usr/include/graphene-1.0/graphene-macros.h
/usr/include/graphene-1.0/graphene-matrix.h
/usr/include/graphene-1.0/graphene-plane.h
/usr/include/graphene-1.0/graphene-point.h
/usr/include/graphene-1.0/graphene-point3d.h
/usr/include/graphene-1.0/graphene-quad.h
/usr/include/graphene-1.0/graphene-quaternion.h
/usr/include/graphene-1.0/graphene-ray.h
/usr/include/graphene-1.0/graphene-rect.h
/usr/include/graphene-1.0/graphene-simd4f.h
/usr/include/graphene-1.0/graphene-simd4x4f.h
/usr/include/graphene-1.0/graphene-size.h
/usr/include/graphene-1.0/graphene-sphere.h
/usr/include/graphene-1.0/graphene-triangle.h
/usr/include/graphene-1.0/graphene-types.h
/usr/include/graphene-1.0/graphene-vec2.h
/usr/include/graphene-1.0/graphene-vec3.h
/usr/include/graphene-1.0/graphene-vec4.h
/usr/include/graphene-1.0/graphene-version-macros.h
/usr/include/graphene-1.0/graphene-version.h
/usr/include/graphene-1.0/graphene.h
/usr/lib64/graphene-1.0/include/graphene-config.h
/usr/lib64/libgraphene-1.0.so
/usr/lib64/pkgconfig/graphene-1.0.pc
/usr/lib64/pkgconfig/graphene-gobject-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgraphene-1.0.so.0
/usr/lib64/libgraphene-1.0.so.0.800.2

%files license
%defattr(-,root,root,-)
/usr/share/doc/graphene/LICENSE
