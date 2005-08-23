# Conditional build:
%bcond_without	local_metadata
%bcond_without	python
%bcond_without	xiph
#
Summary:	Stream directory browser
Summary(pl):	Przegl±darka katalogów strumieni
Name:		streamtuner
Version:	0.99.99
Release:	1
License:	Free
Group:		X11/Applications/Sound
Source0:	http://savannah.nongnu.org/download/streamtuner/%{name}-%{version}.tar.gz
# Source0-md5:	2027b7c34e85b594524b0b4351c14362
Patch0:		%{name}-am.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.nongnu.org/streamtuner/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.10.8
BuildRequires:	gnome-common >= 2.4.0
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	libtool
%{?with_xiph:BuildRequires:	libxml2-devel}
BuildRequires:	pkgconfig
%if %{with python}
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	python-pygtk-devel >= 1:2.4.0
%endif
BuildRequires:	scrollkeeper
%{?with_local_metadata:BuildRequires:	taglib-devel >= 1.3}
Requires:	gtk+2 >= 2:2.4.4
Requires:	%{name}-input = %{version}-%{release}
Conflicts:	streamtuner < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Streamtuner is a stream directory browser. Through the use of a plugin
system, it offers an intuitive GTK+2 interface to Internet radio
directories such as SHOUTcast and Live365.

%description -l pl
Streamtuner jest przegl±dark± katalogów strumieni. Dziêki systemowi
wtyczek program oferuje intuicyjny interfejs GTK+2 do katalogów
internetowych strumieni radiowych takich jak SHOUTcast czy Live365.

%package devel
Summary:	Header files for streamtuner
Summary(pl):	Pliki nag³ówkowe streamtuner
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.4.4

%description devel
Header files for streamtuner.

%description devel -l pl
Pliki nag³ówkowe streamtuner.

%package live365
Summary:	Live365 plugin for streamtuner
Summary(pl):	Wtyczka Live365 dla streamtunera
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}
Conflicts:	streamtuner-live365 < %{version}

%description live365
Live365 plugin for streamtuner.

%description live365 -l pl
Wtyczka Live365 dla streamtunera.

%package local
Summary:	Plugin for streamtuner providing access to local music collection
Summary(pl):	Wtyczka dla streamtunera daj±ca dostêp do lokalnej kolekcji muzyki
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}
Conflicts:	streamtuner-local < %{version}

%description local
Plugin providing access to your local music collection. It can read
and modify ID3 and Vorbis metadata.

%description local -l pl
Wtyczka dla streamtunera daj±ca dostêp do lokalnej kolekcji muzyki.
Dziêki tej wtyczce mo¿na odczytywaæ i modyfikowaæ metadane ID3 i
Vorbis.

%package python
Summary:	Plugin for streamtuner providing an embedded Python interpreter
Summary(pl):	Wtyczka dla streamtunera dostarczaj±ca wbudowany interpreter Pythona
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Conflicts:	streamtuner-python < %{version}

%description python
Plugin for streamtuner providing an embedded Python interpreter.

%description python -l pl
Wtyczka dla streamtunera dostarczaj±ca wbudowany interpreter Pythona.

%package shoutcast
Summary:	SHOUTcast plugin for streamtuner
Summary(pl):	Wtyczka SHOUTcast dla streamtunera
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}
Conflicts:	streamtuner < %{version}

%description shoutcast
SHOUTcast plugin for streamtuner.

%description shoutcast -l pl
Wtyczka SHOUTcast dla streamtunera.

%package xiph
Summary:	Plugin for streamtuner implementing a dir.xiph.org handler
Summary(pl):	Wtyczka dla streamtunera implementuj±ca obs³ugê dir.xiph.org
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}
Conflicts:	streamtuner-xiph < %{version}

%description xiph
Plugin for streamtuner implementing a dir.xiph.org handler.

%description xiph -l pl
Wtyczka dla streamtunera implementuj±ca obs³ugê dir.xiph.org.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
gnome-doc-common
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{!?with_local_metadata:--disable-local-metadata} \
	%{!?with_python:--disable-python} \
	%{!?with_xiph:--disable-xiph} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.{a,la}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/bin/scrollkeeper-update
%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ui
%exclude %{_datadir}/%{name}/ui/live365.png
%exclude %{_datadir}/%{name}/ui/local.png
%exclude %{_datadir}/%{name}/ui/python.png
%exclude %{_datadir}/%{name}/ui/shoutcast.png
%exclude %{_datadir}/%{name}/ui/xiph.png
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_gtkdocdir}/%{name}
%{_pkgconfigdir}/*.pc

%files live365
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/live365.so
%{_datadir}/%{name}/ui/live365.png

%files local
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/local.so
%{_datadir}/%{name}/ui/local.png

%if %{with python}
%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/python.so
%{_datadir}/%{name}/ui/python.png
%dir %{_datadir}/%{name}/python
%{_datadir}/%{name}/python/*
%endif

%files shoutcast
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/shoutcast.so
%{_datadir}/%{name}/ui/shoutcast.png

%if %{with xiph}
%files xiph
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/plugins/xiph.so
%{_datadir}/%{name}/ui/xiph.png
%endif
