column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Income at Entry'), 
        dcc.Slider(
            id='entry_income', 
            min=0, 
            max=3000, 
            step=100, 
            value=2000, 
            marks={n: str(n) for n in range(0,3000,100)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Length of Time Homeless in days'), 
        dcc.Slider(
            id='length_homeless', 
            min=0, 
            max=400, 
            step=10, 
            value=40, 
            marks={n: str(n) for n in range(0,400,10)}, 
            className='mb-5', 
        ), 
        
        dcc.Markdown('#### Total HouseHold Size'), 
        dcc.Slider(
            id='CaseMembers', 
            min=1, 
            max=10, 
            step=1, 
            value=3, 
            marks={n: str(n) for n in range(1,10,1)}, 
            className='mb-5', 
        ), 
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Exit To Permanent Housing', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('entry_income', 'value'), Input('length_homeless', 'value'), Input('CaseMembers', 'value')],
)
def predict(entry_income, length_homeless, CaseMembers):
    df = pd.DataFrame(
        columns=['entry_income', 'length_homeless', 'CaseMembers'], 
        data=[[entry_income, length_homeless, CaseMembers]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.0f} years'