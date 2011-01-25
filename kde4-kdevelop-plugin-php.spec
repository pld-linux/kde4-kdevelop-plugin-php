%define		orgname		kdevelop-php
%define		_kdevelopver	4.2.0
%define		_state		stable
%define		kdever		4.6.0
%define		qtver		4.7.1

Summary:	PHP plugins for kdevelop
Summary(pl.UTF-8):	Wtyczki PHP dla kdevelop
Name:		kde4-kdevelop-plugin-php
Version:	1.2.0
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/kdevelop/%{_kdevelopver}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	fc48c194e7b87c9fd0850b2d7fc2a78b
Source1:	ftp://ftp.kde.org/pub/kde/%{_state}/kdevelop/%{_kdevelopver}/src/%{orgname}-docs-%{version}.tar.bz2
# Source1-md5:	5e7c3c33d9e0767bbf3b3df02147dfae
URL:		http://www.kdevelop.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	kde4-kdevelop-pg-qt
BuildRequires:	kde4-kdevplatform-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	kde4-kdevelop >= %{_kdevelopver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP plugins for kdevelop.

%description -l pl.UTF-8
Wtyczki PHP dla kdevelop.

%prep
%setup -q -n %{orgname}-%{version} -a1

%build
install -d build
cd build
%cmake \
	../
%{__make}
cd ../

cd %{orgname}-docs-%{version}
install -d build
cd build
%cmake \
	../
%{__make}
cd ../

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%{__make} -C %{orgname}-docs-%{version}/build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f kdevelop-php.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kdevphpdocs.so
%attr(755,root,root) %{_libdir}/kde4/kdevphpdocs_config.so
%attr(755,root,root) %{_libdir}/kde4/kdevphplanguagesupport.so
%attr(755,root,root) %{_libdir}/libkdev4phpcompletion.so
%attr(755,root,root) %{_libdir}/libkdev4phpduchain.so
%attr(755,root,root) %{_libdir}/libkdev4phpparser.so
%dir %{_datadir}/apps/kdevappwizard
%dir %{_datadir}/apps/kdevappwizard/templates
%{_datadir}/apps/kdevappwizard/templates/simple_phpapp.tar.bz2
%dir %{_datadir}/apps/kdevphpsupport
%{_datadir}/apps/kdevphpsupport/phpfunctions.php
%{_datadir}/config.kcfg/phpdocssettings.kcfg
%{_datadir}/kde4/services/kdevphpsupport.desktop
%{_datadir}/kde4/services/kdevphpdocs.desktop
%{_datadir}/kde4/services/kdevphpdocs_config.desktop
