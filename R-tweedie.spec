%global packname  tweedie
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.1.7
Release:          1
Summary:          Tweedie exponential family models
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/tweedie_2.1.7.tar.gz
Requires:         R-statmod 
Requires:         R-fBasics 
Requires:         R-stabledist
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-statmod
BuildRequires:    R-fBasics 
BuildRequires:    R-stabledist

%description
Maximum likelihood computations for Tweedie families.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs


%changelog
* Sat Feb 18 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1.1-1
+ Revision: 776605
- Import R-tweedie
- Import R-tweedie


