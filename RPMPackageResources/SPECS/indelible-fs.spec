Name:	indelible-fs	
Version:	@REVISION@
Release:	1%{?dist}
Summary:	Indelible FS Storage Management System Core File system
Group:		System Environment/Daemons
License:	Apache
URL:		http://www.indeliblefs.com
Source:		%{name}-%{version}.tar.gz

BuildRequires:	java-1.6.0-openjdk, ant >= 1.8, avahi-devel
Requires:	postgresql-server >= 8.4, avahi, avahi-tools, avahi-libs, java-1.6.0-openjdk

%description
Indelible FS is a distributed, scalable file system.  Replication and versioning (i.e. backup) is built-in as is
deduplication.
%prep
%setup

%build
cd %{_builddir}/%{name}-%{version}/IndelibleFS-Linux
ant buildDist

%install
echo %{buildroot}
cd %{_builddir}/%{name}-%{version}/IndelibleFS-Linux
ant -DrpmInstallDir='%{buildroot}' install-rh

%files
/etc/init/
/usr/bin/
/usr/lib/igeek/indelible-fs/
/usr/share/igeek/indelible-fs/

%changelog

%clean
echo "Not cleaning"