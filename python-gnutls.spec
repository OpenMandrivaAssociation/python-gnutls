Name:		python-gnutls
Version:	1.2.4
Release:	1
Group:		Sciences/Other
License:	LGPL
Summary:	Python wrapper for the GNUTLS library
Source0:	python-gnutls-%{version}.tar.gz
URL:		http://pypi.python.org/pypi/python-gnutls
BuildRequires:	libgnutls-devel
BuildRequires:	python-devel

%description
This package provides a high level object oriented wrapper around libgnutls,
as well as low level bindings to the GNUTLS types and functions via ctypes.
The high level wrapper hides the details of accessing the GNUTLS library
via ctypes behind a set of classes that encapsulate GNUTLS sessions,
certificates and credentials and expose them to python applications using
a simple API.

%prep
%setup -q

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot}

%files
%py_platsitedir/gnutls
%py_platsitedir/*.egg-info
