# revision 17256
# category Package
# catalog-ctan /macros/latex/contrib/multirow
# catalog-date 2010-02-27 22:08:17 +0100
# catalog-license lppl1
# catalog-version 1.6
Name:		texlive-multirow
Version:	1.6
Release:	4
Summary:	Create tabular cells spanning multiple rows
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multirow
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multirow.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multirow.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package has a lot of flexibility, including an option for
specifying an entry at the "natural" width of its text. The
package is distributed with the bigdelim and bigstrut packages,
which can be used to advantage with \multirow cells.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/multirow/bigdelim.sty
%{_texmfdistdir}/tex/latex/multirow/bigstrut.sty
%{_texmfdistdir}/tex/latex/multirow/multirow.sty
%doc %{_texmfdistdir}/doc/latex/multirow/README
%doc %{_texmfdistdir}/doc/latex/multirow/miscdoc.sty
%doc %{_texmfdistdir}/doc/latex/multirow/multirow.pdf
%doc %{_texmfdistdir}/doc/latex/multirow/multirow.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-2
+ Revision: 754233
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 719087
- texlive-multirow
- texlive-multirow
- texlive-multirow
- texlive-multirow

