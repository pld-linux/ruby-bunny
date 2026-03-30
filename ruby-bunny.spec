%define pkgname bunny
Summary:	Synchronous Ruby AMQP 0.9.1 client
Name:		ruby-%{pkgname}
Version:	2.24.0
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	https://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	7def408414cb9be28d9c827889a98d60
URL:		http://rubybunny.info
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	ruby-amq-protocol >= 2.3
Requires:	ruby-sorted_set >= 1.0.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy to use, feature complete Ruby client for RabbitMQ 3.9 and later
versions.

%prep
%setup -q -n %{pkgname}-%{version}

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
%doc README.md
%{ruby_vendorlibdir}/amq
%{ruby_vendorlibdir}/bunny.rb
%{ruby_vendorlibdir}/bunny
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
