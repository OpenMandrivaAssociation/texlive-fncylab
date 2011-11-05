# revision 17382
# category Package
# catalog-ctan /macros/latex/contrib/fncylab
# catalog-date 2010-03-09 12:54:42 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-fncylab
Version:	1.0
Release:	1
Summary:	Alter the format of \label references
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fncylab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fncylab.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fncylab.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
LaTeX provides a mechanism for altering the appearance of
references to labels, but it's somewhat flawed, and requires
that the user manipulate internal commands. The package fixes
the flaw in LaTeX, and provides a \labelformat command for
changing the format of references to labels. The package also
provides a \Ref command to make reference to such redefined
labels at the start of a sentence.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fncylab/fncylab.sty
%doc %{_texmfdistdir}/doc/latex/fncylab/fncylab-example.tex
%doc %{_texmfdistdir}/doc/latex/fncylab/fncylab.pdf
%doc %{_texmfdistdir}/doc/latex/fncylab/fncylab.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
