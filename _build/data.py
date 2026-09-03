# -*- coding: utf-8 -*-
"""Single source of truth for all site content.

Every design in build.py renders from this file, so the content is
guaranteed identical across all 10 candidates.
"""

PROFILE = {
    "name": "Zechu (Steven) Li",
    "first": "Zechu",
    "last": "Li",
    "photo": "files/scholar_photo.jpg",   # pulled from the Google Scholar profile
    "role": "PhD Student",
    "affil": "PEARL Lab, TU Darmstadt",
    "tagline": "Reinforcement learning &middot; Robotics &middot; Scalable systems",
    "keywords": ["Reinforcement Learning", "Robotics", "Massively Parallel Simulation", "Scalable Systems"],
    "bio": [
        'I am a PhD student at <a href="https://pearl-lab.com/" target="_blank" rel="noopener">PEARL Lab</a>, advised by Prof. <a href="https://pearl-lab.com/people/georgia-chalvatzaki/" target="_blank" rel="noopener">Georgia Chalvatzaki</a> since October 2024, '
        'and currently a Student Researcher at <a href="https://deepmind.google/" target="_blank" rel="noopener">Google DeepMind</a> in London. Previously, I was a visiting '
        'researcher at <a href="https://www.csail.mit.edu/" target="_blank" rel="noopener">MIT CSAIL</a> with Prof. <a href="http://people.csail.mit.edu/pulkitag/" target="_blank" rel="noopener">Pulkit Agrawal</a> and interned at <a href="https://www.dexmate.ai/" target="_blank" rel="noopener">DexMate</a> and <a href="https://www.idea.edu.cn/" target="_blank" rel="noopener">IDEA Research</a>.',

        'My research focuses on robot learning and reinforcement learning, with particular '
        'interests in scalable simulation, dexterous and humanoid manipulation, and agentic '
        'systems for automating robot learning.',

        'I received my bachelor&rsquo;s degree in computer science from <a href="https://www.columbia.edu/" target="_blank" rel="noopener">Columbia University</a> in May 2022. '
        'During my undergraduate studies, I was fortunate to work with Prof. <a href="https://www.ee.columbia.edu/~wangx/" target="_blank" rel="noopener">Xiaodong Wang</a>, '
        'Prof. <a href="https://scholar.google.com.au/citations?user=Q5oC62EAAAAJ&amp;hl=en" target="_blank" rel="noopener">Anwar Walid</a>, and Prof. <a href="https://sharondi-columbia.wixsite.com/ditectlab" target="_blank" rel="noopener">Sharon (Xuan) Di</a>.',
    ],
    "links": [
        ("Email", "mailto:zl2993@columbia.edu", "far fa-envelope"),
        ("Google Scholar", "https://scholar.google.com/citations?user=FI_6by0AAAAJ&hl=en", "ai ai-google-scholar"),
        ("GitHub", "https://github.com/supersglzc", "fab fa-github"),
        ("X", "https://x.com/softraeh", "fab fa-x-twitter"),
        ("LinkedIn", "https://www.linkedin.com/in/zechu-li-66a7741b3/", "fab fa-linkedin"),
    ],
}

# ---------------------------------------------------------------------------
# Author shorthands: (display name, url or None, is_me)
# ---------------------------------------------------------------------------
ME = ("Zechu Li", None, True)
ME_EQ = ("Zechu Li*", None, True)

A = {
    "yufeng":       ("Yufeng Jin", "https://yufengjin.github.io/"),
    "yufeng_eq":    ("Yufeng Jin*", "https://yufengjin.github.io/"),
    "xyliu":        ("Xiao-Yang Liu", "http://www.tensorlet.org/"),
    "xyliu_eq":     ("Xiao-Yang Liu*", "http://www.tensorlet.org/"),
    "puze":         ("Puze Liu", "https://puzeliu.github.io/"),
    "vignesh":      ("Vignesh Prasad", "https://pearl-lab.com/vignesh-prasad/"),
    "carlo":        ("Carlo D'Eramo", "https://www.caidas.uni-wuerzburg.de/rlcdm/team/carlo-deramo/"),
    "georgia":      ("Georgia Chalvatzaki", "https://pearl-lab.com/people/georgia-chalvatzaki/"),
    "jan":          ("Jan Peters", "https://www.ias.informatik.tu-darmstadt.de/Team/JanPeters"),
    "daniel_o":     ("Daniel Ordoñez Apraez", "https://daniel-ordonez-apraez.netlify.app/"),
    "semini":       ("Claudio Semini", "https://www.iit.it/people-details/-/people/claudio-semini"),
    "celik":        ("Onur Celik", "https://onur4229.github.io/"),
    "blessing":     ("Denis Blessing", "https://denisbless.github.io/"),
    "geli":         ("Ge Li", "https://brucegeli.github.io/"),
    "palenicek":    ("Daniel Palenicek", "https://www.ias.informatik.tu-darmstadt.de/Team/DanielPalenicek"),
    "neumann":      ("Gerhard Neumann", "https://alr.iar.kit.edu/21_65.php"),
    "rickmer":      ("Rickmer Krohn", None),
    "taochen":      ("Tao Chen", "https://taochenshh.github.io/"),
    "taochen_eq":   ("Tao Chen*", "https://taochenshh.github.io/"),
    "anurag":       ("Anurag Ajay", "https://anuragajay.github.io/"),
    "pulkit":       ("Pulkit Agrawal", "https://people.csail.mit.edu/pulkitag/"),
    "pulkit_eq":    ("Pulkit Agrawal*", "https://people.csail.mit.edu/pulkitag/"),
    "marcel":       ("Marcel Torne", "https://marceltorne.github.io/"),
    "anthony":      ("Anthony Simeonov", "https://anthonysimeonov.github.io/"),
    "april":        ("April Chan", None),
    "abhishek_eq":  ("Abhishek Gupta*", "https://abhishekunique.github.io/"),
    "zwhong":       ("Zhang-Wei Hong", "https://williamd4112.github.io/"),
    "xdwang":       ("Xiaodong Wang", "https://www.ee.columbia.edu/~wangx/"),
    "jianfei_eq":   ("Jianfei Guo*", "https://ventusff.github.io/"),
    "xiaogang":     ("Xiaogang Jia", "https://xiaogangjia.github.io/Personal_Website/"),
    "yudeng":       ("Yu Deng", "https://yudeng321.github.io/"),
    "hanliu":       ("Han Liu", "https://www.linkedin.com/in/han-liu-697a442aa/"),
    "weiran":       ("Weiran Liao", None),
    "franzius":     ("Mathias Franzius", "https://www.linkedin.com/in/mathias-franzius-86b17b2b4/"),
    "niklas":       ("Niklas Funk", "https://niklasfunk.com/"),
    "xuchen":       ("Xu Chen", None),
    "sharon":       ("Sharon (Xuan) Di", "https://sharondi-columbia.wixsite.com/ditectlab"),
    "shixun":       ("Shixun Wu", None),
    "jiahao":       ("Jiahao Zheng", None),
    "zhaoran":      ("Zhaoran Wang", "https://zhaoranwang.github.io/"),
    "anwar":        ("Anwar Walid", "https://scholar.google.com.au/citations?user=Q5oC62EAAAAJ&hl=en"),
    "anwar_bell":   ("Anwar Walid", "http://www.bell-labs.com/about/researcher-profiles/anwarwalid/#gref"),
    "jianguo":      ("Jian Guo", "https://idea.edu.cn/person/guojian/"),
    "zhuoran":      ("Zhuoran Yang", "https://www.princeton.edu/~zy6/"),
    "jordan":       ("Michael Jordan", "http://people.eecs.berkeley.edu/~jordan/"),
    "yiming":       ("Yiming Fang", None),
    "liuqing":      ("Liuqing Yang", None),
}


def a(key):
    """Expand an author shorthand into (name, url, is_me)."""
    name, url = A[key]
    return (name, url, False)


SELECTED = [
    {
        "id": "harbor",
        "title": "HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning",
        "authors": [ME, a("yufeng"), a("xyliu"), a("puze"), a("vignesh"), a("carlo"), a("georgia")],
        "venue": "arXiv", "year": "2026",
        "media": ("img", "images/harbor_demo.webp"),   # animated WebP: autoplays + loops on its own
        "href": "https://arxiv.org/abs/2606.08610",
        "links": [("paper", "https://arxiv.org/abs/2606.08610"),
                  ("website", "https://supersglzc.github.io/harbor-rl/"),
                  ("code", "https://github.com/supersglzc/harbor-rl")],
        "desc": "Automates the end-to-end robot RL workflow, from package installation to policy tuning.",
    },
    {
        "id": "bimanual-datagen",
        "title": "Scalable Multi-Task Data Generation via Reinforcement Learning for Language-Conditioned Bimanual Dexterous Manipulation",
        "authors": [ME, a("yufeng"), a("puze"), a("jan"), a("georgia")],
        "venue": "IROS", "year": "2026",
        "media": ("img", "images/iros.jpg"),
        "href": "https://arxiv.org/abs/2606.22471",
        "links": [("paper", "https://arxiv.org/abs/2606.22471")],
        "desc": "Generates multi-task demonstrations for language-conditioned bimanual manipulation via RL.",
    },
    {
        "id": "symdex",
        "title": "Morphologically Symmetric Reinforcement Learning for Ambidextrous Bimanual Manipulation",
        "authors": [ME, a("yufeng"), a("daniel_o"), a("semini"), a("puze"), a("georgia")],
        "venue": "CoRL", "year": "2025",
        "media": ("video", "images/symdex.mp4"),
        "href": "https://arxiv.org/abs/2505.05287",
        "links": [("paper", "https://arxiv.org/abs/2505.05287"),
                  ("website", "https://supersglzc.github.io/projects/symdex/"),
                  ("code", "https://github.com/supersglzc/symdex")],
        "desc": "Exploits morphological symmetry to learn ambidextrous bimanual manipulation.",
    },
    {
        "id": "dime",
        "title": "DIME: Diffusion-Based Maximum Entropy Reinforcement Learning",
        "authors": [a("celik"), ME, a("blessing"), a("geli"), a("palenicek"), a("jan"), a("georgia"), a("neumann")],
        "venue": "ICML", "year": "2025",
        "media": ("img", "images/DIME.png"),
        "href": "https://arxiv.org/abs/2502.02316",
        "links": [("paper", "https://arxiv.org/abs/2502.02316"),
                  ("website", "https://alrhub.github.io/dime-website/"),
                  ("code", "https://github.com/ALRhub/DIME")],
        "desc": "Trains diffusion policies with maximum-entropy RL, reaching state-of-the-art returns.",
    },
    {
        "id": "ddiffpg",
        "title": "Learning Multimodal Behaviors from Scratch with Diffusion Policy Gradient",
        "authors": [ME, a("rickmer"), a("taochen"), a("anurag"), a("pulkit"), a("georgia")],
        "venue": "NeurIPS", "year": "2024",
        "media": ("img", "images/ddiffpg.png"),
        "href": "https://arxiv.org/abs/2406.00681",
        "links": [("paper", "https://arxiv.org/abs/2406.00681"),
                  ("website", "https://supersglzc.github.io/projects/ddiffpg/"),
                  ("code", "https://github.com/supersglzc/ddiffpg")],
        "desc": "Learns multimodal diffusion policies from scratch, without demonstrations.",
    },
    {
        "id": "rialto",
        "title": "Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation",
        "authors": [a("marcel"), a("anthony"), ME, a("april"), a("taochen"), a("abhishek_eq"), a("pulkit_eq")],
        "venue": "Robotics: Science and Systems (RSS)", "venue_short": "RSS", "year": "2024",
        "media": ("img", "images/realto.gif"),
        "href": "http://arxiv.org/abs/2403.03949",
        "links": [("paper", "http://arxiv.org/abs/2403.03949"),
                  ("website", "https://real-to-sim-to-real.github.io/RialTo/"),
                  ("code", "https://github.com/real-to-sim-to-real/RialToPolicyLearning")],
        "desc": "Robustifies real-world policies by fine-tuning them in digital twins built on the fly.",
    },
    {
        "id": "pql",
        "title": "Parallel Q-Learning: Scaling Off-policy Reinforcement Learning under Massively Parallel Simulation",
        "authors": [ME_EQ, a("taochen_eq"), a("zwhong"), a("anurag"), a("pulkit")],
        "venue": "ICML", "year": "2023",
        "media": ("img", "files/parallel_scheme.png"),
        "href": "https://openreview.net/pdf?id=vFvw8EzQNLy",
        "links": [("paper", "https://openreview.net/pdf?id=vFvw8EzQNLy"),
                  ("code", "https://github.com/Improbable-AI/pql")],
        "desc": "Scales off-policy RL to 10,000+ parallel environments.",
    },
    {
        "id": "hmc",
        "title": "Homomorphic Matrix Completion",
        "authors": [a("xyliu_eq"), ME_EQ, a("xdwang")],
        "venue": "NeurIPS", "year": "2022",
        "media": ("img", "files/distributed_scheme.png"),
        "href": "https://proceedings.neurips.cc/paper_files/paper/2022/hash/4f550cb7b30b59553e50cd08a9dbf068-Abstract-Conference.html",
        "links": [("paper", "https://proceedings.neurips.cc/paper_files/paper/2022/hash/4f550cb7b30b59553e50cd08a9dbf068-Abstract-Conference.html")],
        "desc": "Achieves exact matrix completion under differential privacy, at the cost of more samples.",
    },
]

OTHER = [
    {
        "id": "nautilus",
        "title": "Nautilus: From One Prompt to Plug-and-Play Robot Learning",
        "authors": [a("yufeng_eq"), a("jianfei_eq"), a("xiaogang"), a("yudeng"), ME, a("hanliu"),
                    a("weiran"), a("vignesh"), a("franzius"), a("neumann"), a("georgia")],
        "venue": "arXiv", "year": "2026",
        "media": ("img", "images/nautilus.png"),
        "href": "https://arxiv.org/abs/2605.11665v1",
        "links": [("paper", "https://arxiv.org/abs/2605.11665v1"),
                  ("website", "https://yufengjin.github.io/projects/nautilus/")],
        "desc": "Turns a single prompt into reproduction, evaluation, fine-tuning, and deployment workflows.",
    },
    {
        "id": "se3poseflow",
        "title": "SE(3)-PoseFlow: Estimating 6D Pose Distributions for Uncertainty-Aware Robotic Manipulation",
        "authors": [a("yufeng"), a("niklas"), a("vignesh"), ME, a("franzius"), a("jan"), a("georgia")],
        "venue": "ICRA", "year": "2026",
        "media": ("img", "images/se3poseflow.webp"),
        "href": "https://arxiv.org/abs/2511.01501",
        "links": [("paper", "https://arxiv.org/abs/2511.01501"),
                  ("website", "https://yufengjin.github.io/projects/se3-poseflow/")],
        "desc": "Estimates full 6D pose distributions via flow matching on SE(3) for uncertainty-aware manipulation.",
    },
    {
        "id": "sdd",
        "title": "Social Learning for Sequential Driving Dilemmas",
        "authors": [a("xuchen"), a("sharon"), ME],
        "venue": "Games", "year": "2023",
        "media": ("img", "images/games-14-00041-g001.png"),
        "href": "https://www.mdpi.com/2073-4336/14/3/41",
        "links": [("paper", "https://www.mdpi.com/2073-4336/14/3/41")],
        "desc": "Identifies when social dilemmas arise in autonomous vehicles&rsquo; sequential decisions.",
    },
    {
        "id": "kspin",
        "title": "Stationary Deep Reinforcement Learning with Quantum K-spin Hamiltonian Equation",
        "authors": [a("xyliu_eq"), ME_EQ, a("shixun"), a("xdwang")],
        "venue": "Workshop on Physics for Machine Learning, ICLR", "venue_short": "ICLR Workshop", "year": "2023",
        "media": ("img", "files/gradient.png"),
        "href": "https://openreview.net/pdf?id=LVum7knUA7g",
        "links": [("paper", "https://openreview.net/pdf?id=LVum7knUA7g")],
        "desc": "Adds a quantum K-spin Hamiltonian regularizer that steers policies toward better optima.",
    },
    {
        "id": "social-markov",
        "title": "Social Learning In Markov Games: Empowering Autonomous Driving",
        "authors": [a("xuchen"), ME, a("sharon")],
        "venue": "IEEE Intelligent Vehicles Symposium (IV)", "venue_short": "IEEE IV", "year": "2022",
        "media": ("img", "images/social_learning.png"),
        "href": "https://ieeexplore.ieee.org/document/9827289",
        "links": [("paper", "https://ieeexplore.ieee.org/document/9827289"),
                  ("code", "https://github.com/supersglzc/Social-Learning")],
        "desc": "Studies how autonomous vehicles form social norms through RL in Markov games.",
    },
    {
        "id": "finrl-podracer",
        "title": "FinRL-Podracer: High Performance and Scalable Deep Reinforcement Learning for Quantitative Finance",
        "authors": [ME, a("xyliu"), a("jiahao"), a("zhaoran"), a("anwar"), a("jianguo")],
        "venue": "ACM International Conference on AI in Finance (ICAIF)", "venue_short": "ICAIF", "year": "2021",
        "media": ("img", "images/finrl_podracer.png"),
        "href": "https://dl.acm.org/doi/10.1145/3490354.3494413",
        "links": [("paper", "https://dl.acm.org/doi/10.1145/3490354.3494413"),
                  ("code", "https://github.com/AI4Finance-Foundation/FinRL_Podracer")],
        "desc": "Trains a NASDAQ-100 trading agent in 10 minutes on 80 A100 GPUs.",
    },
    {
        "id": "elegantrl-podracer",
        "title": "ElegantRL-Podracer: Scalable and Elastic Library for Cloud-native Deep Reinforcement Learning",
        "authors": [a("xyliu_eq"), ME_EQ, a("zhuoran"), a("jiahao"), a("zhaoran"), a("anwar"), a("jianguo"), a("jordan")],
        "venue": "Deep Reinforcement Learning Workshop, NeurIPS", "venue_short": "NeurIPS Workshop", "year": "2021",
        "media": ("img", "images/erl_podracer.png"),
        "href": "https://arxiv.org/pdf/2112.05923.pdf",
        "links": [("paper", "https://arxiv.org/pdf/2112.05923.pdf"),
                  ("code", "https://github.com/AI4Finance-Foundation/ElegantRL")],
        "desc": "Scales cloud-native DRL training across millions of GPU cores.",
    },
]

BLOG_POSTS = [
    ("ElegantRL: Much More Stable Deep Reinforcement Learning Algorithms than Stable-Baseline3",
     "https://medium.com/mlearning-ai/elegantrl-much-much-more-stable-than-stable-baseline3-f096533c26db",
     "MLearning.ai", "Mar. 3, 2022"),
    ("ElegantRL-Podracer: A Scalable and Elastic Library for Cloud-Native Deep Reinforcement Learning",
     "https://elegantrl.medium.com/elegantrl-podracer-scalable-and-elastic-library-for-cloud-native-deep-reinforcement-learning-bafda6f7fbe0",
     "Towards data science", "Dec. 11, 2021"),
    ("ElegantRL: Mastering PPO Algorithms",
     "https://medium.com/@elegantrl/elegantrl-mastering-the-ppo-algorithm-part-i-9f36bc47b791",
     "Towards data science", "May. 3, 2021"),
    ("ElegantRL Demo: Stock Trading Using DDPG (Part II)",
     "https://medium.com/mlearning-ai/elegantrl-demo-stock-trading-using-ddpg-part-ii-d3d97e01999f",
     "MLearning.ai", "Apr. 19, 2021"),
    ("ElegantRL Demo: Stock Trading Using DDPG (Part I)",
     "https://elegantrl.medium.com/elegantrl-demo-stock-trading-using-ddpg-part-i-e77d7dc9d208",
     "MLearning.ai", "Mar. 28, 2021"),
    ("ElegantRL-Helloworld: A Lightweight and Stable Deep Reinforcement Learning Library",
     "https://towardsdatascience.com/elegantrl-a-lightweight-and-stable-deep-reinforcement-learning-library-95cef5f3460b",
     "Towards data science", "Mar. 4, 2021"),
]

PROJECTS = [
    {
        "id": "finrl",
        "title": "FinRL: Financial Reinforcement Learning",
        "media": ("img", "images/finrl.png"),
        "href": "https://github.com/AI4Finance-Foundation/FinRL",
        "links": [("project page", "https://finrl.readthedocs.io/en/latest/index.html"),
                  ("code", "https://github.com/AI4Finance-Foundation/FinRL"),
],
        "desc": "Brings deep reinforcement learning to quantitative finance and automated trading.",
        "repo": "AI4Finance-Foundation/FinRL",
        "stars": 16207,   # GitHub API, re-run to refresh
    },
    {
        "id": "elegantrl",
        "title": "ElegantRL “小雅”: Massively Parallel Library for Cloud-native Deep Reinforcement Learning",
        "media": ("img", "images/elegantrl.jpg"),
        "href": "https://github.com/AI4Finance-Foundation/ElegantRL",
        "links": [("project page", "https://elegantrl.readthedocs.io/en/latest/index.html"),
                  ("code", "https://github.com/AI4Finance-Foundation/ElegantRL"),
],
        "desc": "Runs massively parallel DRL training on cloud-native infrastructure.",
        "repo": "AI4Finance-Foundation/ElegantRL",
        "stars": 4360,   # GitHub API, re-run to refresh
        "contrib_intro": "As a leader of this project, I have been contributing to",
        "contrib": [
            "develop a series of large-scale training frameworks,",
            "implemente SOTA algorithms and techniques,",
            "build the documentation website.",
        ],
        "blog_intro": "Starting from Mar. 2021, I started to write tutorial blogs for the community,",
        "blog": BLOG_POSTS,
    },
]

BOOK = [
    {
        "id": "tensor-book",
        "title": "High-performance Tensor Decompositions for Compressing and Accelerating Deep Neural Networks",
        "authors": [a("xyliu"), a("yiming"), a("liuqing"), ME, a("anwar_bell")],
        "venue": "Tensors for Data Processing, Elsevier", "venue_short": "Elsevier", "year": "2021",
        "media": ("img", "images/book.jpg"),
        "href": "https://www.sciencedirect.com/science/article/pii/B9780128244470000157",
        "links": [("chapter", "https://www.sciencedirect.com/science/article/pii/B9780128244470000157"),
                  ("book", "https://www.elsevier.com/books/tensors-for-data-processing/liu/978-0-12-824447-0")],
        "desc": "Compresses and accelerates neural networks with high-performance tensor decompositions.",
    },
]

FOOTER_CREDIT = ('<a href="https://people.eecs.berkeley.edu/~barron/" target="_blank" rel="noopener">'
                 'This guy makes a nice webpage.</a>')

GA_ID = "UA-79592980-2"

DESIGNS = [
    ("01", "terminal",   "Terminal",      "Monospace CLI aesthetic, dark, prompt-driven sections."),
    ("02", "editorial",  "Editorial",     "Swiss grid, big type, hairline rules, numbered sections."),
    ("03", "lab",        "Lab",           "Dark glass cards with a soft accent glow."),
    ("04", "blueprint",  "Blueprint",     "Technical-drawing look: graph paper, crosshairs, callouts."),
    ("05", "paper",      "Paper",         "LaTeX-flavored serif typesetting, quiet and academic."),
    ("06", "dock",       "Dock",          "Sticky profile sidebar with a scroll-spy nav."),
    ("07", "timeline",   "Timeline",      "Vertical spine, publications threaded by year."),
    ("08", "gallery",    "Gallery",        "Image-forward responsive card grid."),
    ("09", "ide",        "IDE",           "Code-editor chrome: tabs, gutter, syntax accents."),
    ("10", "brutalist",  "Brutalist",     "High-contrast blocks, oversized numerals, hard edges."),
]
