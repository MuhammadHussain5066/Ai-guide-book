<!-- Sync Impact Report:
Version change: 1.0.1 → 1.1.0
List of modified principles: All principles adapted for book context.
Added sections: Target Audience, Technology Stack
Removed sections: None
Templates requiring updates:
  ⚠ .specify/templates/plan-template.md
  ⚠ .specify/templates/spec-template.md
  ⚠ .specify/templates/tasks-template.md
  ✅ .specify/templates/commands/sp.constitution.md
  ⚠ CLAUDE.md
Follow-up TODOs: Adapt project templates for book context.
-->
# Physical AI Book Constitution

## Core Principles

### I. Clarity & Accessibility
Content MUST be clear, concise, and accessible to the target audience. Technical jargon should be explained or avoided where possible.

### II. Practicality & Hands-on Learning
The book MUST prioritize practical examples, hands-on projects, and real-world applications to facilitate active learning.

### III. Accuracy & Verification
All technical information, code examples, and theoretical concepts MUST be rigorously verified for accuracy and kept up-to-date with current best practices.

### IV. Foundational Understanding
The book MUST build a strong foundational understanding of Physical AI concepts before diving into advanced topics.

### V. Ethical Considerations
Ethical implications and responsible development practices related to Physical AI MUST be discussed throughout the book.

## Target Audience

Beginner to intermediate engineers, researchers, and hobbyists interested in building and understanding intelligent physical systems. Readers are assumed to have a basic understanding of Python programming and fundamental AI/ML concepts.

## Technology Stack

- **Core Languages**: Python (primary), C++ (for low-level hardware interaction where necessary).
- **Frameworks/Libraries**: TensorFlow, PyTorch, ROS (Robot Operating System), OpenCV, Gym (for reinforcement learning environments).
- **Hardware Platforms**: Raspberry Pi, Arduino, basic robotic kits (e.g., wheeled robots, simple manipulators) for hands-on projects.

## Content Development Workflow & Governance

- **Content Review**: All chapters and code examples MUST be reviewed for technical accuracy, clarity, and pedagogical effectiveness.
- **Example Testing**: All code examples and projects MUST be thoroughly tested on the specified hardware platforms to ensure functionality and reproducibility.
- **Documentation**: Clear explanations, diagrams, and step-by-step instructions MUST accompany all complex concepts and practical implementations.
- **Version Control**: The book's source content and code examples MUST be managed using Git.

## Governance

This Constitution supersedes all other content development practices. Amendments require documentation, team approval, and a clear migration plan. All content contributions MUST verify compliance with these principles. Any deviations from these principles MUST be explicitly justified and approved by the editorial board.

**Version**: 1.1.0 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-06
