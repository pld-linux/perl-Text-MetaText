%include	/usr/lib/rpm/macros.perl
Summary:	Text-MetaText perl module
Summary(pl):	Modu³ perla Text-MetaText
Name:		perl-Text-MetaText
Version:	0.22
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-MetaText-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-File-Tools
BuildRequires:	perl-TimeDate
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Text-MetaText perl module.

%description -l pl
Modu³ perla Text-MetaText.

%prep
%setup -q -n Text-MetaText-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/MetaText
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
        Changes README Todo Features

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,Todo,Features}.gz
%attr(755,root,root) %{_bindir}/metapage

%{perl_sitelib}/Text/MetaText.pm
%{perl_sitelib}/Text/MetaText
%{perl_sitearch}/auto/Text/MetaText

%{_mandir}/man[13]/*
