%define		_realname xmms-nebulus
Summary:	Nebulus visualization plugin
Summary(pl.UTF-8):	Wtyczka wizualizacji Nebulus dla XMMS-a
Name:		xmms-visualization-nebulus
Version:	0.8.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://nebulus.tuxfamily.org/%{_realname}-%{version}.tar.bz2
# Source0-md5:	07c15281a5e2e242a79536c07982cf5a
URL:		http://nebulus.tuxfamily.org/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.5
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.7
Requires:	OpenGL
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Nebulus is an OpenGL visual plugin for XMMS.

%description -l pl.UTF-8
Nebulus jest wtyczką wizualizacji dla XMMS-a opartą o OpenGL.

%prep
%setup -q -n %{_realname}-%{version}

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{_realname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_realname}.lang
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{xmms_visualization_plugindir}/*
