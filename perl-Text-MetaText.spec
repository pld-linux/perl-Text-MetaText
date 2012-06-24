%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	MetaText
Summary:	Text::MetaText Perl module
Summary(cs):	Modul Text::MetaText pro Perl
Summary(da):	Perlmodul Text::MetaText
Summary(de):	Text::MetaText Perl Modul
Summary(es):	M�dulo de Perl Text::MetaText
Summary(fr):	Module Perl Text::MetaText
Summary(it):	Modulo di Perl Text::MetaText
Summary(ja):	Text::MetaText Perl �⥸�塼��
Summary(ko):	Text::MetaText �� ����
Summary(no):	Perlmodul Text::MetaText
Summary(pl):	Modu� Perla Text::MetaText
Summary(pt):	M�dulo de Perl Text::MetaText
Summary(pt_BR):	M�dulo Perl Text::MetaText
Summary(ru):	������ ��� Perl Text::MetaText
Summary(sv):	Text::MetaText Perlmodul
Summary(uk):	������ ��� Perl Text::MetaText
Summary(zh_CN):	Text::MetaText Perl ģ��
Name:		perl-Text-MetaText
Version:	0.22
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-File-Recurse
BuildRequires:	perl-TimeDate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::MetaText Perl module.

%description -l cs
Modul Text::MetaText pro Perl

%description -l da
Perlmodul Text::MetaText

%description -l de
Text::MetaText Perl Modul

%description -l es
M�dulo de Perl Text::MetaText

%description -l fr
Module Perl Text::MetaText

%description -l it
Modulo di Perl Text::MetaText

%description -l ja
Text::MetaText Perl �⥸�塼��

%description -l ko
Text::MetaText �� ����

%description -l no
Perlmodul Text::MetaText

%description -l pl
Modu� Perla Text::MetaText.

%description -l pt
M�dulo de Perl Text::MetaText

%description -l pt_BR
M�dulo Perl Text::MetaText

%description -l ru
������ ��� Perl Text::MetaText

%description -l sv
Text::MetaText Perlmodul

%description -l uk
������ ��� Perl Text::MetaText

%description -l zh_CN
Text::MetaText Perl ģ��

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo Features
%attr(755,root,root) %{_bindir}/metapage
%{perl_sitelib}/Text/MetaText.pm
%{perl_sitelib}/Text/MetaText
%{_mandir}/man[13]/*
