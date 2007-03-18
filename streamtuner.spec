Summary:	Stream directory browser
Summary(pl):	Przegl±darka katalogów strumieni
Name:		streamtuner
Version:	0.12.5
Release:	2
License:	Free
Group:		X11/Applications/Sound
Source0:	http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	4782aa87bda0bbefbeb172ee2b3bfecf
Patch0:		%{name}-am.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.nongnu.org/streamtuner/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.10.8
BuildRequires:	gnome-common >= 2.4.0
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	libtool
BuildRequires:	scrollkeeper
Requires:	gtk+2 >= 2:2.4.4
Requires:	xmms
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
	--enable-shoutcast=plugin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.{a,la}

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_omf_dest_dir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_pkgconfigdir}/*.pc
