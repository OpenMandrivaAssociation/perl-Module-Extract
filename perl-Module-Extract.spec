%define upstream_name    Module-Extract
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Base class for working with Perl distributions
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Archive::Extract)
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
*Module::Extract* is a convenience base class for creating module that work
with Perl distributions.

Its purpose is to take care of the mechanisms of locating and extracting a
Perl distribution so that your module can do something specific to the
distribution.

This module was originally created to provide an abstraction for the
extraction logic for both the Module::Inspector manpage and the Module::P4P
manpage and to allow additional features to be added in the future without
having to modify both of them, because the general problem of "locate,
download, and expand a distribution" is one that is almost ideal for adding
additional features down the line.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.10.0-2mdv2011.0
+ Revision: 655051
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 401631
- rebuild using %%perl_convert_version
- fixed license field

* Tue Jan 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.01-1mdv2009.1
+ Revision: 329065
- import perl-Module-Extract


* Tue Jan 13 2009 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist

