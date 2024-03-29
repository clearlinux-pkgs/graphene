#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : graphene
Version  : 1.10.8
Release  : 35
URL      : https://download.gnome.org/sources/graphene/1.10/graphene-1.10.8.tar.xz
Source0  : https://download.gnome.org/sources/graphene/1.10/graphene-1.10.8.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause MIT
Requires: graphene-data = %{version}-%{release}
Requires: graphene-lib = %{version}-%{release}
Requires: graphene-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : glib-dev
BuildRequires : glibc-bin
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Graphene
###  A thin layer of types for graphic libraries
![Linux Build](https://github.com/ebassi/graphene/workflows/Ubuntu%20Build/badge.svg)
![MSVC Build](https://github.com/ebassi/graphene/workflows/MSVC%20Build/badge.svg)
![MSYS2 Build](https://github.com/ebassi/graphene/workflows/MSYS2%20Build/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/ebassi/graphene/badge.svg?branch=master)](https://coveralls.io/github/ebassi/graphene?branch=master)
[![License: MIT](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

%package data
Summary: data components for the graphene package.
Group: Data

%description data
data components for the graphene package.


%package dev
Summary: dev components for the graphene package.
Group: Development
Requires: graphene-lib = %{version}-%{release}
Requires: graphene-data = %{version}-%{release}
Provides: graphene-devel = %{version}-%{release}
Requires: graphene = %{version}-%{release}

%description dev
dev components for the graphene package.


%package lib
Summary: lib components for the graphene package.
Group: Libraries
Requires: graphene-data = %{version}-%{release}
Requires: graphene-license = %{version}-%{release}

%description lib
lib components for the graphene package.


%package license
Summary: license components for the graphene package.
Group: Default

%description license
license components for the graphene package.


%package tests
Summary: tests components for the graphene package.
Group: Default
Requires: graphene = %{version}-%{release}

%description tests
tests components for the graphene package.


%prep
%setup -q -n graphene-1.10.8
cd %{_builddir}/graphene-1.10.8
pushd ..
cp -a graphene-1.10.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685543815
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/graphene
cp %{_builddir}/graphene-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/graphene/53ca621a56a9ded7d6ba2f3e608a43515875783b || :
cp %{_builddir}/graphene-%{version}/subprojects/mutest/LICENSE.txt %{buildroot}/usr/share/package-licenses/graphene/13869509cd8e339104f92084c841c24a72ca2034 || :
cp %{_builddir}/graphene-%{version}/subprojects/mutest/docs/LICENSE.markdeep.txt %{buildroot}/usr/share/package-licenses/graphene/25997556cbd0a4d064057d267c81c8d8b60e7be4 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Graphene-1.0.typelib
/usr/share/gir-1.0/*.gir

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
/V3/usr/lib64/libgraphene-1.0.so.0.1000.8
/usr/lib64/libgraphene-1.0.so.0
/usr/lib64/libgraphene-1.0.so.0.1000.8

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/graphene/13869509cd8e339104f92084c841c24a72ca2034
/usr/share/package-licenses/graphene/25997556cbd0a4d064057d267c81c8d8b60e7be4
/usr/share/package-licenses/graphene/53ca621a56a9ded7d6ba2f3e608a43515875783b

%files tests
%defattr(-,root,root,-)
/V3/usr/libexec/installed-tests/graphene-1.0/box
/V3/usr/libexec/installed-tests/graphene-1.0/euler
/V3/usr/libexec/installed-tests/graphene-1.0/frustum
/V3/usr/libexec/installed-tests/graphene-1.0/matrix
/V3/usr/libexec/installed-tests/graphene-1.0/plane
/V3/usr/libexec/installed-tests/graphene-1.0/point
/V3/usr/libexec/installed-tests/graphene-1.0/point3d
/V3/usr/libexec/installed-tests/graphene-1.0/quad
/V3/usr/libexec/installed-tests/graphene-1.0/quaternion
/V3/usr/libexec/installed-tests/graphene-1.0/ray
/V3/usr/libexec/installed-tests/graphene-1.0/rect
/V3/usr/libexec/installed-tests/graphene-1.0/simd
/V3/usr/libexec/installed-tests/graphene-1.0/size
/V3/usr/libexec/installed-tests/graphene-1.0/sphere
/V3/usr/libexec/installed-tests/graphene-1.0/triangle
/V3/usr/libexec/installed-tests/graphene-1.0/vec2
/V3/usr/libexec/installed-tests/graphene-1.0/vec3
/V3/usr/libexec/installed-tests/graphene-1.0/vec4
/usr/libexec/installed-tests/graphene-1.0/box
/usr/libexec/installed-tests/graphene-1.0/euler
/usr/libexec/installed-tests/graphene-1.0/frustum
/usr/libexec/installed-tests/graphene-1.0/introspection.py
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
/usr/share/installed-tests/graphene-1.0/box.test
/usr/share/installed-tests/graphene-1.0/euler.test
/usr/share/installed-tests/graphene-1.0/frustum.test
/usr/share/installed-tests/graphene-1.0/introspection.py.test
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
