=================
mermaid 使用示例
=================


流程图
=========

.. mermaid::

    flowchart TD
        A[Start] --> B{Is it?}
        B -- Yes --> C[OK]
        C --> D[Rethink]
        D --> B
        B -- No ----> E[End]

.. mermaid::

    flowchart TB
        c1-->a2
        subgraph one
        a1-->a2
        end
        subgraph two
        b1-->b2
        end
        subgraph three
        c1-->c2
        end

序列图
=========

.. mermaid::

   sequenceDiagram
      participant Alice
      participant Bob
      Alice->John: Hello John, how are you?
      loop Healthcheck
          John->John: Fight against hypochondria
      end
      Note right of John: Rational thoughts <br/>prevail...
      John-->Alice: Great!
      John->Bob: How about you?
      Bob-->John: Jolly good!

.. mermaid::

    sequenceDiagram
        participant Alice
        participant John

        rect rgb(191, 223, 255)
        note right of Alice: Alice calls John.
        Alice->>+John: Hello John, how are you?
        rect rgb(200, 150, 255)
        Alice->>+John: John, can you hear me?
        John-->>-Alice: Hi Alice, I can hear you!
        end
        John-->>-Alice: I feel great!
        end
        Alice ->>+ John: Did you want to go to the game tonight?
        John -->>- Alice: Yeah! See you there.

自动生成类图
================
.. autoclasstree:: sphinx.util.DownloadFiles sphinx.util.ExtensionError
   :full:

.. autoclasstree:: sphinx.util
