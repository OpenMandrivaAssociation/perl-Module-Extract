%define upstream_name    Module-Extract
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Base class for working with Perl distributions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Archive::Extract)
BuildRequires: perl(Carp)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*

