%include	/usr/lib/rpm/macros.perl
Summary:	Text-MetaText perl module
Summary(pl):	Modu³ perla Text-MetaText
Name:		perl-Text-MetaText
Version:	0.22
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-MetaText-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-File-Tools
BuildRequires:	perl-TimeDate
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-MetaText perl module.

%description -l pl
Modu³ perla Text-MetaText.

%prep
%setup -q -n Text-MetaText-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README Todo Features

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/metapage
%{perl_sitelib}/Text/MetaText.pm
%{perl_sitelib}/Text/MetaText
%{_mandir}/man[13]/*
