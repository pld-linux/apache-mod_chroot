%define		mod_name	chroot
%define 	apxs		/usr/sbin/apxs
Summary:	Apache module: makes running Apache in a secure chroot environment easy
Summary(pl):	Modu� Apache'a do uruchamiania serwera w bezpiecznym �rodowisku chroot
Name:		apache-mod_%{mod_name}
Version:	0.4
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://core.segfault.pl/~hobbit/mod_chroot/dist/mod_chroot-%{version}.tar.gz
# Source0-md5:	abd2c8209b61b2a2fecdf10a61051060
URL:		http://core.segfault.pl/~hobbit/mod_chroot/
BuildRequires:	%{apxs}
BuildRequires:	apache-devel
Requires(post,preun):	%{apxs}
Requires:	apache
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pkglibdir	%(%{apxs} -q LIBEXECDIR)

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

install -D .libs/mod_%{mod_name}.so $RPM_BUILD_ROOT%{_pkglibdir}/mod_%{mod_name}.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CAVEATS ChangeLog INSTALL README
%attr(755,root,root) %{_pkglibdir}/*.so
