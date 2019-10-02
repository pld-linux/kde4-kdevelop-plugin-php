%define		orgname		kdevelop-php
%define		_kdevelopver	4.7.0
%define		_state		stable
%define		kdever		4.10.0
%define		qtver		4.8.0

Summary:	PHP plugins for kdevelop
Summary(pl.UTF-8):	Wtyczki PHP dla kdevelop
Name:		kde4-kdevelop-plugin-php
Version:	1.7.0
Release:	2
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/kdevelop/%{_kdevelopver}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	d1e87ff5d7417ead1143471957eeeae2
Source1:	ftp://ftp.kde.org/pub/kde/%{_state}/kdevelop/%{_kdevelopver}/src/%{orgname}-docs-%{version}.tar.xz
# Source1-md5:	1f6f391d6afe1e708d491eb267de199d
URL:		http://www.kdevelop.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-tools
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
%attr(755,root,root) %{_libdir}/kde4/kdevphpunitprovider.so
%attr(755,root,root) %{_libdir}/libkdev4phpcompletion.so
%attr(755,root,root) %{_libdir}/libkdev4phpduchain.so
%attr(755,root,root) %{_libdir}/libkdev4phpparser.so
%dir %{_datadir}/apps/kdevappwizard
%dir %{_datadir}/apps/kdevappwizard/templates
%{_datadir}/apps/kdevappwizard/templates/simple_phpapp.tar.bz2
%dir %{_datadir}/apps/kdevphpsupport
%{_datadir}/apps/kdevphpsupport/phpfunctions.php
%{_datadir}/apps/kdevphpsupport/phpunitdeclarations.php
%{_datadir}/config.kcfg/phpdocssettings.kcfg
%{_datadir}/kde4/services/kdevphpsupport.desktop
%{_datadir}/kde4/services/kdevphpdocs.desktop
%{_datadir}/kde4/services/kdevphpdocs_config.desktop
%{_datadir}/kde4/services/kdevphpunitprovider.desktop
