%define		mod_name	chroot
%define 	apxs		/usr/sbin/apxs
Summary:	Apache module: makes running Apache in a secure chroot environment easy
Summary(pl):	Modu� Apache'a do uruchamiania serwera w bezpiecznym �rodowisku chroot
Name:		apache-mod_%{mod_name}
Version:	0.5
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://core.segfault.pl/~hobbit/mod_chroot/dist/mod_chroot-%{version}.tar.gz
# Source0-md5:	d72716052faa3bdd3371210f26b13f38
URL:		http://core.segfault.pl/~hobbit/mod_chroot/
BuildRequires:	%{apxs}
BuildRequires:	apache-devel >= 2.0
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	apache(modules-api) = %apache_modules_api
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR 2>/dev/null)
%define		_sysconfdir	%(%{apxs} -q SYSCONFDIR 2>/dev/null)

%description
mod_chroot makes running Apache in a secure chroot environment easy.
You don't need to create a special directory hierarchy containing
/dev, /lib, /etc...

%description -l pl
mod_chroot u�atwia uruchamianie Apache'a w bezpiecznym �rodowisku
chroot. Nie trzeba tworzy� specjalnej hierarchii katalog�w /dev, /lib,
/etc, itp.

%prep
%setup -q -n mod_%{mod_name}-%{version}

%build
%{apxs} -c mod_%{mod_name}.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkglibdir},%{_sysconfdir}/httpd.conf}

install .libs/mod_%{mod_name}.so $RPM_BUILD_ROOT%{_pkglibdir}/mod_%{mod_name}.so
echo 'LoadModule %{mod_name}_module modules/mod_%{mod_name}.so' > \
	$RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf/90_mod_%{mod_name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q httpd restart

%postun
if [ "$1" = "0" ]; then
	%service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%doc CAVEATS ChangeLog INSTALL README
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf/*_mod_%{mod_name}.conf
%attr(755,root,root) %{_pkglibdir}/*.so
