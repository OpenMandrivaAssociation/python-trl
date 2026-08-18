Name:		python-trl
Version:	1.10.0
Release:	1
Summary:	Train transformer language models with reinforcement learning
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/huggingface/trl
Source0:	https://files.pythonhosted.org/packages/source/t/trl/trl-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

Requires:	python%{pyver}dist(accelerate)
Requires:	python%{pyver}dist(datasets)
Requires:	python%{pyver}dist(jinja2)
Requires:	python%{pyver}dist(packaging)
Requires:	python%{pyver}dist(transformers)
Recommends:	python%{pyver}dist(peft)
Recommends:	python%{pyver}dist(torch)

%description
TRL implements SFT, DPO, ORPO, PPO and other post-training methods on
top of transformers + accelerate. Used by Unsloth and gguf-edit for
preference training (prompt / chosen / rejected).

%files
%doc README.md
%license LICENSE
%{_bindir}/trl
%{py_sitedir}/trl
%{py_sitedir}/trl-*.*-info
