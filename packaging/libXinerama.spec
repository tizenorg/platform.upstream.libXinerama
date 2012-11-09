Name:           libXinerama
Version:        1.1.2
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          System Environment/Libraries

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)

%description
X.Org X11 libXinerama runtime library

%package devel
Summary:        X
Group:          Development/Libraries
Requires:       %{name} = %{version}
Provides:       libxinerama-devel

%description devel
X.Org X11 libXinerama development package

%prep
%setup -q

%build

%configure --disable-static \
	       LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed"
make %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/libXinerama.so.1
%{_libdir}/libXinerama.so.1.0.0

%files devel
%defattr(-,root,root,-)
%{_libdir}/libXinerama.so
%{_libdir}/pkgconfig/xinerama.pc
%{_includedir}/X11/extensions/Xinerama.h
%{_includedir}/X11/extensions/panoramiXext.h
