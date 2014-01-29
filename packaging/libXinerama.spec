%bcond_with x

Name:           libXinerama
Version:        1.1.2
Release:        1
License:        MIT
Summary:        Xinerama protocol library
Url:            http://www.x.org
Group:          Graphics/X Window System
Source0:        %{name}-%{version}.tar.bz2
Source1001: 	libXinerama.manifest

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%if !%{with x}
ExclusiveArch:
%endif

%description
X.Org X11 libXinerama runtime library

%package devel
Summary:        Xinerama protocol library
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
X.Org X11 libXinerama development package

%prep
%setup -q
cp %{SOURCE1001} .

%build

%configure --disable-static
make %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libXinerama.so.1
%{_libdir}/libXinerama.so.1.0.0

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_libdir}/libXinerama.so
%{_libdir}/pkgconfig/xinerama.pc
%{_includedir}/X11/extensions/Xinerama.h
%{_includedir}/X11/extensions/panoramiXext.h
