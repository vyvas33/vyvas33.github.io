// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "About",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-projects",
          title: "projects",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-resume",
          title: "Resume",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/assets/pdf/Resume.pdf";
          },
        },{id: "projects-articulated-mobile-robot",
          title: 'Articulated Mobile Robot',
          description: "A modular center-articulated multi-modal robot for complex environments",
          section: "Projects",handler: () => {
              window.location.href = "/projects/articulated_mobile_robot/";
            },},{id: "projects-gesture-controlled-sma-actuated-robotic-hand",
          title: 'Gesture Controlled SMA Actuated Robotic Hand',
          description: "A robotic hand actuated by shape memory alloy springs and controlled using a gesture glove.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/gesture_controlled_sma_robotic_hand/";
            },},{id: "projects-locomimic",
          title: 'LocoMimic',
          description: "Learning to walk using reinforcement learning.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/locomimic/";
            },},{id: "projects-neuromuscular-models",
          title: 'Neuromuscular Models',
          description: "Hill type muscle models and reflex driven hopping",
          section: "Projects",handler: () => {
              window.location.href = "/projects/neuromuscular_models/";
            },},{id: "projects-robotic-lower-limb-prosthesis-control",
          title: 'Robotic Lower-Limb Prosthesis Control',
          description: "Sensing, estimation and control for a powered knee-ankle prosthesis",
          section: "Projects",handler: () => {
              window.location.href = "/projects/prosthesis/";
            },},{id: "projects-heat-transfer-characteristics-of-synthetic-jets",
          title: 'Heat Transfer Characteristics of Synthetic Jets',
          description: "An experimental study of elliptic synthetic jets with high aspect ratios",
          section: "Projects",handler: () => {
              window.location.href = "/projects/synthetic_jets/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%76%79%76%61%73%32%30%30%32@%67%6D%61%69%6C.%63%6F%6D", "_blank");
        },
      },{
        id: 'social-instagram',
        title: 'Instagram',
        section: 'Socials',
        handler: () => {
          window.open("https://instagram.com/vyvaswath_", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/vyvaswath", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
