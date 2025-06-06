%define		module	pycups
Summary:	Set of Python bindings for the CUPS API
Summary(pl.UTF-8):	Zbiór wiązań Pythona do API CUPS-a
Name:		python3-%{module}
Version:	2.0.4
Release:	1
License:	GPL v2+
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pycups/%{module}-%{version}.tar.gz
# Source0-md5:	a4e9bcdc2012fcff660e0806416a1fb3
URL:		http://cyberelk.net/tim/software/pycups/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	cups-devel >= 1.2.1
BuildRequires:	epydoc
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	rpm-pythonprov
Requires:	python3-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides Python bindings for the CUPS API, known as
pycups. It was written for use with system-config-printer, but can be
put to other uses as well.

%description -l pl.UTF-8
Ten pakiet udostępnia wiązania Pythona do API CUPS-a, znane jako
pycups. Został napisany z myślą o pakiecie system-config-printer, ale
może mieć także inne zastosowania.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{py3_sitedir}/cups.cpython-*.so
%{py3_sitedir}/pycups-%{version}-py*.egg-info
