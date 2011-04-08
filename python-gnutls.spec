Name:		python-gnutls
Version:	1.2.0
Release:	%mkrel 3
Group:		Sciences/Other
License:	LGPL
Summary:	Python wrapper for the GNUTLS library
Source:		python-gnutls-%{version}.tar.gz
URL:		http://pypi.python.org/pypi/python-gnutls
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libgnutls-devel
BuildRequires:	python-devel

Patch0:		python-gnutls-1.2.0-gnutls-2.12.1-deprecated.patch

%description
This package provides a high level object oriented wrapper around libgnutls,
as well as low level bindings to the GNUTLS types and functions via ctypes.
The high level wrapper hides the details of accessing the GNUTLS library
via ctypes behind a set of classes that encapsulate GNUTLS sessions,
certificates and credentials and expose them to python applications using
a simple API.

%prep
%setup -q
%patch0 -p1

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%py_platsitedir/gnutls
%py_platsitedir/*.egg-info
