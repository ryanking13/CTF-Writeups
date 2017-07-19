import json

lv1 = {
    # 000...111
    "initial_state": 'q0',
    "final_states": ['H'],
    "transition_function": [
        # c_state, char_head, n_state, char_push, mov_dir
        ('q0', ' ', 'H', ' ', 'R'),
        ('q1', ' ', 'H', ' ', 'R'),

        ('q0', '0', 'q0', 'x', 'R'),
        ('q0', '1', 'q1', 'y', 'R'),

        ('q1', '1', 'q1', 'y', 'R'),
    ],
    "accepting_states": ['H'],
}


lv2 = {
    # 11... (1 * (13n +2))

    "initial_state": 'q0',
    "final_states": ['H'],
    "transition_function": [
        # c_state, char_head, n_state, char_push, mov_dir
        ('q2', ' ', 'H', ' ', 'R'),

        ('q0', '1', 'q1', '1', 'R'),
        ('q1', '1', 'q2', '1', 'R'),
        ('q2', '1', 'q3', '1', 'R'),
        ('q3', '1', 'q4', '1', 'R'),
        ('q4', '1', 'q5', '1', 'R'),
        ('q5', '1', 'q6', '1', 'R'),
        ('q6', '1', 'q7', '1', 'R'),
        ('q7', '1', 'q8', '1', 'R'),
        ('q8', '1', 'q9', '1', 'R'),
        ('q9', '1', 'q10', '1', 'R'),
        ('q10', '1', 'q11', '1', 'R'),
        ('q11', '1', 'q12', '1', 'R'),
        ('q12', '1', 'q0', '1', 'R'),
    ],
    "accepting_states": ['H'],
}

lv3 = {

    "initial_state": 'q0',
    "final_states": ['H'],
    "transition_function": [
        # c_state, char_head, n_state, char_push, mov_dir

        # empty case
        ('q0', ' ', 'qh', ' ', 'R'),
        ('qh', ' ', 'H', ' ', 'R'),

        # q0 - initial
        ('q0', '0', 'q1', 'x', 'R'),

        # q1 - found '0', now finding corresponding '1'
        ('q1', '0', 'q1', '0', 'R'),
        ('q1', 'y', 'q1', 'y', 'R'),
        ('q1', '1', 'q2', 'y', 'L'),
        # ('q1', ' ') - no 1 left, fail

        # q2 - found corresponding '1', now finding next '0'
        ('q2', 'y', 'q2', 'y', 'L'),
        ('q2', '0', 'q2', '0', 'L'),
        ('q2', 'x', 'q3', 'x', 'R'),

        # if found next '0' -> do q1 again
        ('q3', '0', 'q1', 'x', 'R'),

        # if no more '0' -> q4
        ('q3', 'y', 'q4', 'y', 'R'),

        # q4 -> check if '1' or '0' left
        ('q4', 'y', 'q4', 'y', 'R'),
        # ('q4', '1') - 1 left, fail
        # ('q4', '0') - 0 left, fail

        # success
        ('q4', ' ', 'H', ' ', 'R'),
    ],
    "accepting_states": ['H'],
}

lv4 = {
    # 0... prime
	
    "initial_state": 'q0',
    "final_states": ['H'],
    "transition_function": [
        # c_state, char_head, n_state, char_push, mov_dir

        # Step 0, empty case, '1'  case
        # ('q0', ' ')
        # ('q0', '1')

        # Step1, check if there is '1' ( 00000... --> ...0 )
        ('q0', '0', 'qChkOne', '0', 'R'),
        ('qChkOne', '0', 'qChkOne', '0', 'R'),
        ('qChkOne', ' ', 'qChkSp', ' ', 'L'),

        # Step2, check special cases - [1, 2]
        ('qChkSp', '0', 'qChk1', '0', 'L'),
        # ('qChk1', ' ') - 1 case
        ('qChk1', '0', 'qChk2', '0', 'L'),
        ('qChk2', ' ', 'H', ' ', 'R'),  # 2 case
        ('qChk2', '0', 'qChkDone', '0', 'L'),
        ('qChkDone', '0', 'qChkDone', '0', 'L'),
        ('qChkDone', ' ', 'qFindZero', ' ', 'R'),

        # Step2, fill divisor
        ('qFindZero', '0', 'qFillDivisor', 'x', 'R'),       # go right until find BLANK
        ('qFillDivisor', '0', 'qFillDivisor', '0', 'R'),  # go right until find BLANK
        ('qFillDivisor', 'x', 'qFillDivisor', 'x', 'R'),  # go right until find BLANK
        ('qFillDivisor', 'y', 'qFillDivisor', 'y', 'R'),    # go right until find BLANK
        ('qFillDivisor', ' ', 'qFindZero', 'y', 'L'),       # if found BLANK, change it to y, and go left

        ('qFindZero', 'y', 'qFindZero', 'y', 'L'),   # go left until find 0
        ('qFindZero', 'x', 'qFindZero', 'x', 'L'),   # go left until find 0

        ('qFindZero', ' ', 'qDivisorEndFix', ' ', 'R'),    # done filling divisor

        # Step3, PostFix divisor ( startswith 2, endswith x-1 )
        ('qDivisorEndFix', 'x', 'qDivisorEndFix', 'x', 'R'),
        ('qDivisorEndFix', 'y', 'qDivisorEndFix', 'y', 'R'),
        ('qDivisorEndFix', ' ', 'qDivisorEndFix2', ' ', 'L'),
        ('qDivisorEndFix2', 'y', 'qDivisorStartFix', ' ', 'L'),
        ('qDivisorStartFix', 'y', 'qDivisorStartFix', 'y', 'L'),
        ('qDivisorStartFix', 'x', 'qDivisorStartFix2', 'x', 'R'),
        ('qDivisorStartFix2', 'y', 'qDivisorFixDone', 'd', 'L'),
        ('qDivisorFixDone', 'x', 'qDivisorFixDone', 'x', 'L'),
        ('qDivisorFixDone', ' ', 'qStart', ' ', 'R'),

        # Step4-n, checking prime ( now, head is in starting position )

        # Step4, set Divisor ( divisor = divisor + 1 )
        ('qStart', 'x', 'qDivisorSet', 'x', 'R'),
        ('qDivisorSet', 'x', 'qDivisorSet', 'x', 'R'),
        ('qDivisorSet', 'd', 'qDivisorSet', 'd', 'R'),
        ('qDivisorSet', 'y', 'qDivisorSetDone', 'd', 'R'),

        # Step5, check Divisable

        # Step5-1, mark Divisor
        ('qDivisorSetDone', 'y', 'qMarkDivisor', 'y', 'L'),
        ('qDivisorSetDone', ' ', 'qMarkDivisor', ' ', 'L'),     # may need check
        ('qMarkDivisor', 'dMark', 'qMarkDivisor', 'dMark', 'L'),
        ('qMarkDivisor', 'd', 'qMarkDivisorDone', 'dMark', 'L'),

        # Step5-2, mark Number
        ('qMarkDivisorDone', 'd', 'qMarkDivisorDone', 'd', 'L'),
        ('qMarkDivisorDone', 'dMark', 'qMarkDivisorDone', 'dMark', 'L'),
        ('qMarkDivisorDone', 'xMark', 'qMarkDivisorDone', 'xMark', 'L'),
        ('qMarkDivisorDone', 'x', 'qMarkNumDone', 'xMark', 'R'),

        ('qMarkDivisorDone', ' ', 'qSuccessStep', ' ', 'R'),      # Not divisable

        # Step5-3, mark next Divisor ( then, go to Step 5-1 )
        ('qMarkNumDone', 'xMark', 'qMarkNumDone', 'xMark', 'R'),
        ('qMarkNumDone', 'd', 'qMarkNumDoneDarea', 'd', 'R'),
        ('qMarkNumDoneDarea', 'd', 'qMarkNumDoneDarea', 'd', 'R'),
        ('qMarkNumDoneDarea', 'dMark', 'qMarkDivisor', 'dMark', 'L'),

        # Step5-3-1, if Divisor is fully Marked, reset it
        # ('qMarkNumDone', 'dMark', 'qDivisorReset', 'd', 'R'),
        ('qDivisorReset', 'dMark', 'qDivisorReset', 'd', 'R'),
        ('qDivisorReset', 'x', 'qDivisorReset', 'x', 'R'),
        ('qDivisorReset', 'xMark', 'qDivisorReset', 'xMark', 'R'),
        ('qDivisorReset', 'y', 'qMarkDivisor', 'y', 'L'),
        ('qDivisorReset', ' ', 'qMarkDivisor', ' ', 'L'),

        ('qMarkNumDone', 'dMark', 'qDivisableCheck', 'dMark', 'L'),
        ('qDivisableCheck', 'xMark', 'qDivisableCheck', 'xMark', 'L'),
        ('qDivisableCheck', 'x', 'qDivisorReset', 'x', 'R'),
        # ('qDivisorReset', ' ',)   # number is divisable, fail

        # Step6, if success checking undivisable, unMark All, and update divisor
        ('qSuccessStep', 'xMark', 'qSuccessStep', 'x', 'R'),
        ('qSuccessStep', 'dMark', 'qSuccessStep', 'd', 'R'),
        ('qSuccessStep', 'd', 'qSuccessStep', 'd', 'R'),
        ('qSuccessStep', 'y', 'qDivisorSetDone', 'd', 'R'),

        ('qSuccessStep', ' ', 'H', ' ', 'R'),

    ],
    "accepting_states": ['H'],
}