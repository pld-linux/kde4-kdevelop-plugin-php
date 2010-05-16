%define		orgname		kdevelop-php
%define		_kdevelopver	4.0.0
%define		_state		stable

Summary:	PHP plugins for kdevelop
Summary(pl.UTF-8):	Wtyczki PHP dla kdevelop
Name:		kde4-kdevelop-plugin-php
Version:	1.0.0
Release:	0.2
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/kdevelop/%{_kdevelopver}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	cf132db716b0b0d617e9938281387fff
Source1:	ftp://ftp.kde.org/pub/kde/%{_state}/kdevelop/%{_kdevelopver}/src/%{orgname}-docs-%{version}.tar.bz2
# Source1-md5:	9286ce9a000cb2292c613ad8a7d99cdd
URL:		http://www.kdevelop.org/
BuildRequires:	QtTest-devel
BuildRequires:	automoc4
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	kde4-kdevplatform-devel >= 0.9.97
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
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
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	../
%{__make}
cd ../

cd %{orgname}-docs-%{version}
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
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
%{_datadir}/apps/kdevphpsupport/phpfunctions.php.gz
%{_datadir}/config.kcfg/phpdocssettings.kcfg
%{_datadir}/kde4/services/kdevphpsupport.desktop
%{_datadir}/kde4/services/kdevphpdocs.desktop
%{_datadir}/kde4/services/kdevphpdocs_config.desktop
