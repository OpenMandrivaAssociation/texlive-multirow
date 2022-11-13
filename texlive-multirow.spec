Name:		texlive-multirow
Version:	58396
Release:	1
Summary:	Create tabular cells spanning multiple rows
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/multirow
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multirow.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/multirow.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/multirow
%doc %{_texmfdistdir}/doc/latex/multirow

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
