Summary:        Snapd Compatibility
Name:           snapd-compat
Version:        1
Release:        1%{?dist}
License:        IOL
URL:            https://tauos.co
Source0:	%{name}-%{version}.tar.gz
BuildArch:      noarch
Provides:       snapd-compat(%{version}) = %{release}

Requires:	snapd

%description
snapd support for OSTree-based operating systems

%prep
%setup -q
%build

%install
mkdir -p %{buildroot}/opt/snapd-compat
chmod +x snapd.sh
install snapd.sh %{buildroot}/opt/snapd-compat

mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/
mkdir -p %{buildroot}%{_sysconfdir}/systemd/system/remote-fs.target.wants/
cp snapd-compat.service %{buildroot}%{_sysconfdir}/systemd/system/

%post
ln -sf %{_sysconfdir}/systemd/system/snapd-compat.service %{_sysconfdir}/systemd/system/remote-fs.target.wants/snapd-compat.service

%files
%dir /opt/snapd-compat
/opt/snapd-compat/snapd.sh

%{_sysconfdir}/systemd/system/snapd-compat.service
%ghost %{_sysconfdir}/systemd/system/remote-fs.target.wants/snapd-compat.service

%changelog
