# Copyright (c) liuboxiao. All rights reserved.

from collections import OrderedDict

tree_structure = [
    'Object Detection',
    'Base Model',
]

database = [
    {
        'Name': 'Conditional DETR for Fast Training Convergence',
        'Node': 'Object Detection',
        'Year': 2021,
        'Source': 'ICCV',
        'PDF': 'https://openaccess.thecvf.com/content/ICCV2021/papers/Meng_Conditional_DETR_for_Fast_Training_Convergence_ICCV_2021_paper.pdf',
        'Code': 'https://github.com/Atten4Vis/ConditionalDETR',
        'Authors': ['Depu Meng', 'Xiaokang Chen', 'Zejia Fan', 'Gang Zeng', 'Houqiang Li', 'Yuhui Yuan', 'Lei Sun', 'Jingdong Wang'],
        'Institutions': ['University of Science and Technology of China', 'Peking University', 'Microsoft Research Asia'],
        'Abstract': 'The recently-developed DETR approach applies the transformer encoder and decoder architecture to object detection and achieves promising performance. In this paper, we handle the critical issue, slow training convergence, and present a conditional cross-attention mechanism for fast DETR training. Our approach is motivated by that the cross-attention in DETR relies highly on the content embeddings for localizing the four extremities and predicting the box, which increases the need for high-quality content embeddings and thus the training difficulty. Our approach, named conditional DETR, learns a conditional spatial query from the decoder embedding for decoder multi-head cross-attention. The benefit is that through the conditional spatial query, each cross-attention head is able to attend to a band containing a distinct region, e.g., one object extremity or a region inside the object box. This narrows down the spatial range for localizing the distinct regions for object classification and box regression, thus relaxing the dependence on the content embeddings and easing the training. Empirical results show that conditional DETR converges 6.7x faster for the backbones R50 and R101 and 10x faster for stronger backbones DC5-R50 and DC5-R101. Code is available at https://github.com/Atten4Vis/ConditionalDETR.',
        'Tags': ['DETR'],
        'Discussions':[
            'Use two attention maps instead of one to decouple the semantic and spatial information aggregation.'
        ]
    },
    {
        'Name': 'Rethinking Transformer-based Set Prediction for Object Detection',
        'Node': 'Object Detection',
        'Year': 2021,
        'Source': 'ICCV',
        'PDF': 'https://openaccess.thecvf.com/content/ICCV2021/papers/Sun_Rethinking_Transformer-Based_Set_Prediction_for_Object_Detection_ICCV_2021_paper.pdf',
        'Code': 'https://github.com/Edward-Sun/TSP-Detection',
        'Authors': ['Zhiqing Sun', 'Shengcao Cao', 'Yiming Yang', 'Kris Kitani'],
        'Institutions': ['Carnegie Mellon University'],
        'Abstract': 'DETR is a recently proposed Transformer-based method which views object detection as a set prediction problem and achieves state-of-the-art performance but demands extra-long training time to converge. In this paper, we investigate the causes of the optimization difficulty in the training of DETR. Our examinations reveal several factors contributing to the slow convergence of DETR, primarily the issues with the Hungarian loss and the Transformer crossattention mechanism. To overcome these issues we propose two solutions, namely, TSP-FCOS (Transformer-based Set Prediction with FCOS) and TSP-RCNN (Transformerbased Set Prediction with RCNN). Experimental results show that the proposed methods not only converge much faster than the original DETR, but also significantly outperform DETR and other baselines in terms of detection accuracy.',
        'Tags': ['DETR', 'One Stage', 'Two Stage', 'Anchor Free'],
        'Discussions':[
            'This paper observed that the slow convergence of DETR is mainly due to the smooth attention in the start of training. To obtain object features for bipartite matching, this paper propose to select features from the feature map by a Feature-Of-Interest module in FCOS and RPN in Faster-RCNN.'
        ]
    },
    {
        'Name': 'Fast Convergence of DETR with Spatially Modulated Co-Attention',
        'Node': 'Object Detection',
        'Year': 2021,
        'Source': 'ICCV',
        'PDF': 'http://openaccess.thecvf.com/content/ICCV2021/papers/Gao_Fast_Convergence_of_DETR_With_Spatially_Modulated_Co-Attention_ICCV_2021_paper.pdf',
        'Code': 'https://github.com/gaopengcuhk/SMCA-DETR',
        'Authors': ['Peng Gao, Minghang Zheng, Xiaogang Wang, Jifeng Dai, Hongsheng Li'],
        'Institutions': ['Shanghai AI Laboratory', 'Chinese University of Hong Kong', 'Peking University', 'SenseTime Research'],
        'Abstract': 'The recently proposed Detection Transformer (DETR) model successfully applies Transformer to objects detection and achieves comparable performance with two-stage object detection frameworks, such as Faster-RCNN. However, DETR suffers from its slow convergence. Training DETR [4] from scratch needs 500 epochs to achieve a high accuracy. To accelerate its convergence, we propose a simple yet effective scheme for improving the DETR framework, namely Spatially Modulated Co-Attention (SMCA) mechanism. The core idea of SMCA is to conduct locationaware co-attention in DETR by constraining co-attention responses to be high near initially estimated bounding box locations. Our proposed SMCA increases DETR???s convergence speed by replacing the original co-attention mechanism in the decoder while keeping other operations in DETR unchanged. Furthermore, by integrating multi-head and scale-selection attention designs into SMCA, our fullyfledged SMCA can achieve better performance compared to DETR with a dilated convolution-based backbone (45.6 mAP at 108 epochs vs. 43.3 mAP at 500 epochs). We perform extensive ablation studies on COCO dataset to validate SMCA. Code is released at https://github.com/gaopengcuhk/SMCA-DETR.',
        'Tags': ['DETR'],
        'Discussions':[
            'Use the object queries to generate a Gaussian-like mask to constrain the attention in a local region.'
        ]
    },
    {
        'Name': 'Sparse R-CNN: End-to-End Object Detection with Learnable Proposals',
        'Node': 'Object Detection',
        'Year': 2021,
        'Source': 'CVPR',
        'PDF': 'https://openaccess.thecvf.com/content/CVPR2021/papers/Sun_Sparse_R-CNN_End-to-End_Object_Detection_With_Learnable_Proposals_CVPR_2021_paper.pdf',
        'Code': 'https://github.com/PeizeSun/SparseR-CNN',
        'Authors': ['Peize Sun, Rufeng Zhang, Yi Jiang, Tao Kong, Chenfeng Xu, Wei Zhan, Masayoshi Tomizuka, Lei Li, Zehuan Yuan, Changhu Wang, Ping Luo'],
        'Institutions': ['The University of Hong Kong', 'Tongji University', 'ByteDance AI Lab', 'University of California, Berkeley'],
        'Abstract': 'We present Sparse R-CNN, a purely sparse method for object detection in images. Existing works on object detection heavily rely on dense object candidates, such as k anchor boxes pre-defined on all grids of image feature map of size H ?? W. In our method, however, a fixed sparse set of learned object proposals, total length of N, are provided to object recognition head to perform classification and location. By eliminating HWk (up to hundreds of thousands) hand-designed object candidates to N (e.g. 100) learnable proposals, Sparse R-CNN completely avoids all efforts related to object candidates design and many-toone label assignment. More importantly, final predictions are directly output without non-maximum suppression postprocedure. Sparse R-CNN demonstrates accuracy, run-time and training convergence performance on par with the wellestablished detector baselines on the challenging COCO dataset, e.g., achieving 45.0 AP in standard 3?? training schedule and running at 22 fps using ResNet-50 FPN model. We hope our work could inspire re-thinking the convention of dense prior in object detectors. The code is available at: https://github.com/PeizeSun/SparseR-CNN.',
        'Tags': ['DETR', 'Two Stage'],
        'Discussions':[
            'Use learnable query boxes and features to gather information of instances for detection. The learned position and feature of each box is static at first, and is refined through iterative modules. Dynamic MLPs are utilized to achieve better performance.'
        ]
    },
]

def generate_readme():
    content = {}
    for node in tree_structure:
        content[node] = {}
    for paper in database:
        node = paper['Node']
        assert node in content.keys()
        year = paper['Year']
        if year not in content[node].keys():
            content[node][year] = []
        content[node][year].append(paper)
    
    readme = '# awesome_paper_tree\nOrganize awesome papers in a hierarchical tree.\n'
    for node in content.keys():
        readme += '## {}\n'.format(node)
        content_node = content[node]
        year_list = list(content_node.keys())
        year_list.sort()
        for year in year_list:
            readme += '### {}\n'.format(year)
            for paper in content_node[year]:
                readme += '- {}.\\\n{}.'.format(paper['Name'], paper['Source'])
                readme += ' [PDF]({}).'.format(paper['PDF'])
                readme += ' [Code]({}). Tags:'.format(paper['Code'])
                for tag in paper['Tags']:
                    readme += ' {},'.format(tag)
                readme = readme[:-1] + '.'
                readme += ' <details><summary>More</summary>Authors:'
                for author in paper['Authors']:
                    readme += ' {},'.format(author)
                readme = readme[:-1] + '.'
                readme += '\\\nInstitutions:'
                for institutions in paper['Institutions']:
                    readme += ' {},'.format(institutions)
                readme = readme[:-1] + '.'
                readme += '\\\nAbstract: {}</details>\n'.format(paper['Abstract'])

    with open('README.md', 'w') as f:
        f.write(readme)


if __name__ == "__main__":
    generate_readme()
