%define pkgname bunny
Summary:	Synchronous Ruby AMQP 0.9.1 client
Name:		ruby-%{pkgname}
Version:	0.7.9
Release:	4
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/gems/%{pkgname}-%{version}.gem
# Source0-md5:	9984619cb0bd727485c3bf26a00af336
URL:		http://github.com/ruby-amqp/bunny
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A synchronous Ruby AMQP client that enables interaction with
AMQP-compliant brokers.

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
%setup -q
cp -p %{_datadir}/setup.rb .

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.textile CHANGELOG
%{ruby_vendorlibdir}/bunny.rb
%{ruby_vendorlibdir}/bunny
%{ruby_vendorlibdir}/qrack
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%if 0
%files doc
%defattr(644,root,root,755)
%endif
