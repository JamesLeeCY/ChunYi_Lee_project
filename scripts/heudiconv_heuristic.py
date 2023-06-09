import os


def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes

def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    t1w = create_key('sub-{subject}/anat/sub-{subject}_T1w')
    t2w4task = create_key('sub-{subject}/anat/sub-{subject}_acq-4task_T2w')
    t2w4rest = create_key('sub-{subject}/anat/sub-{subject}_acq-4rest_T2w')
    taskepi = create_key('sub-{subject}/func/sub-{subject}_task-dbb_run-{item:01d}_bold')
    restepi = create_key('sub-{subject}/func/sub-{subject}_task-rest_bold')
    fmap_m = create_key('sub-{subject}/fmap/sub-{subject}_magnitude')
    fmap_p = create_key('sub-{subject}/fmap/sub-{subject}_phasediff')
    dwi = create_key('sub-{subject}/dwi/sub-{subject}_dwi')

    info = {
                t1w: [],
                t2w4task: [],
                t2w4rest: [],
                taskepi: [],
                restepi: [],
                fmap_m:[],
                fmap_p:[],
                dwi:[]
            }
    last_run = len(seqinfo)

    for s in seqinfo:
        if ('MPRAGE' in s.protocol_name) and (s.dim3 == 192) and ('T1' == s.dcm_dir_name):
            info[t1w].append(s.series_id)
        if ('gre_field_mapping' in s.protocol_name) and (s.dim3 == 76) and ('FMAP' == s.dcm_dir_name):
            info[fmap_m].append(s.series_id)
        if ('gre_field_mapping' in s.protocol_name) and (s.dim3 == 38) and ('FMAP_P' == s.dcm_dir_name):
            info[fmap_p].append(s.series_id)
        if ('t2_tse_tra' in s.protocol_name) and (s.dim3 == 38) and (('T2' == s.dcm_dir_name) or 'T2_1' in s.dcm_dir_name):
            info[t2w4task].append(s.series_id)
        if ('t2_tse_tra' in s.protocol_name) and (s.dim3 == 38) and ('T2_CR' == s.dcm_dir_name):
            info[t2w4rest].append(s.series_id)
        if ('ep2d_moco_4mm_' in s.protocol_name) and (s.dim1 == 64) and (s.dim2 == 64) and ('F' in s.dcm_dir_name):
            info[taskepi].append(s.series_id)
        if ('ep2d_moco_4mm_' in s.protocol_name) and ('REST' in s.protocol_name) and (s.dim4 == 240):
            info[restepi].append(s.series_id)
        if ('ep2d_diff_mddw' in s.protocol_name) and (s.dim1 == 78) and (s.dim2 == 78):
            info[dwi].append(s.series_id)

        """
        The namedtuple `s` contains the following fields:

        * total_files_till_now
        * example_dcm_file
        * series_id
        * dcm_dir_name
        * unspecified2
        * unspecified3
        * dim1
        * dim2
        * dim3
        * dim4
        * TR
        * TE
        * protocol_name
        * is_motion_corrected
        * is_derived
        * patient_id
        * study_description
        * referring_physician_name
        * series_description
        * image_type
        """

    return info

