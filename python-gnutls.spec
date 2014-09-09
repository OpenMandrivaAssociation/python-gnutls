%define debug_package %{nil}
Name:		python-gnutls
Version:	2.0.1
Release:	1
Group:		Sciences/Other
License:	LGPL
Summary:	Python wrapper for the GNUTLS library
Source0:	https://pypi.python.org/packages/source/p/python-gnutls/%{name}-%{version}.tar.gz
URL:		http://pypi.python.org/pypi/python-gnutls
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	python-devel

%description
This package provides a high level object oriented wrapper around libgnutls,
as well as low level bindings to the GNUTLS types and functions via ctypes.
The high level wrapper hides the details of accessing the GNUTLS library
via ctypes behind a set of classes that encapsulate GNUTLS sessions,
certificates and credentials and expose them to python applications using
a simple API.

%package -n	python2-gnutls
Summary:	Python wrapper for the GNUTLS library
Group:		Sciences/Other

%description
This package provides a high level object oriented wrapper around libgnutls,
as well as low level bindings to the GNUTLS types and functions via ctypes.
The high level wrapper hides the details of accessing the GNUTLS library
via ctypes behind a set of classes that encapsulate GNUTLS sessions,
certificates and credentials and expose them to python applications using
a simple API.


%prep
%setup -q
cp -a . %{py2dir}

%build
%__python setup.py build
pushd %{py2dir}
%{__python2} setup.py build
popd

%install
%__python setup.py install --root=%{buildroot}
pushd %{py2dir}
%__python2 setup.py install --root=%{buildroot}
popd

%files
%{python_sitelib}/gnutls
%{python_sitelib}/*.egg-info

%files -n python2-gnutls
%{python2_sitelib}/gnutls
%{python2_sitelib}/*.egg-info
