#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Text
%define		pnam	MetaText
Summary:	Text::MetaText - meta-language for processing "template" text files
Summary(pl.UTF-8):	Text::MetaText - metajęzyk do przetwarzania szablonów tekstowych
Name:		perl-Text-MetaText
Version:	0.22
Release:	14
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4a2b5d120459dcb678cac876c99fa805
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-File-Recurse
BuildRequires:	perl-TimeDate
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MetaText is a text processing and markup meta-language which can
be used for processing "template" files. This module is a Perl 5
extension implementing a MetaText object class which processes
text files, interpreting and acting on the embedded MetaText
directives within.

Like a glorified pre-processor, MetaText can: include files,
define and substitute variable values, execute conditional
actions based on variables, call other Perl functions or object
methods and capture the resulting output back into the document,
and more. It can format the resulting output of any of these
operations in a number of ways. The objects, and inherently, the
format and symantics of the MetaText langauge itself, are highly
configurable.

%description -l pl.UTF-8
MetaText to metajęzyk do przetwarzania tekstu i oznaczeń, który można
używać do przetwarzania plików "szablonów". Ten moduł jest
rozszerzeniem Perla 5 implementującym klasę obiektu MetaText
przetwarzającego pliki tekstowe, interpretującego i działającego na
osadzonych w nich dyrektywach MetaTextu.

Podobnie jak każdy zachwalany preprocesor MetaText może: dołączać
pliki, definiować i podstawiać wartości zmiennych, wykonywać akcje
warunkowe w oparciu o zmienne, wywoływać inne funkcje Perla lub
metody obiektów i przechwytywać ich wyniki z powrotem do dokumentu
i wiele innych. Wyjście dowolnej z operacji może być formatowane na
wiele sposobów. Obiekty i związany z nimi format oraz semantyka
samego języka MetaText są wysoce konfigurowalne.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mv t/exec.t{,.whythiscrapfails}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Todo Features
%attr(755,root,root) %{_bindir}/metapage
%{perl_vendorlib}/Text/MetaText.pm
%{perl_vendorlib}/Text/MetaText
%{_mandir}/man[13]/*
